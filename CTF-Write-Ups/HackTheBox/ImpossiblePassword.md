# Impossible Password Writeup
## Materials
To start off with we were provided with:
- 1 Linux x86 ELF binary file

## Steps
First I ran the binary in my WSL environment, and running it prompts for user input, then displays the input and exits.

After opening the binary in IDA, I saw two `strcmp` functions that would probably be the main points of focus while reversing this.

A quick view of the hex shows an interesting string hardcoded in the program: 
`53 75 70 65 72 53 65 4B 72 65 74 4B 65 79` => `"SuperSeKretKey"`

This is indeed the key used for the first `strcmp`, but I needed to figure out the second one. I opened it in Ghidra to view the C code for the relevant section:
```c
void FUN_0040085d(void)

{
  int iVar1;
  char *__s2;
  undefined local_48;
  undefined local_47;
  undefined local_46;
  undefined local_45;
  undefined local_44;
  undefined local_43;
  undefined local_42;
  undefined local_41;
  undefined local_40;
  undefined local_3f;
  undefined local_3e;
  undefined local_3d;
  undefined local_3c;
  undefined local_3b;
  undefined local_3a;
  undefined local_39;
  undefined local_38;
  undefined local_37;
  undefined local_36;
  undefined local_35;
  char local_28 [20];
  int local_14;
  char *local_10;
  
  local_10 = "SuperSeKretKey";
  local_48 = 0x41;
  local_47 = 0x5d;
  local_46 = 0x4b;
  local_45 = 0x72;
  local_44 = 0x3d;
  local_43 = 0x39;
  local_42 = 0x6b;
  local_41 = 0x30;
  local_40 = 0x3d;
  local_3f = 0x30;
  local_3e = 0x6f;
  local_3d = 0x30;
  local_3c = 0x3b;
  local_3b = 0x6b;
  local_3a = 0x31;
  local_39 = 0x3f;
  local_38 = 0x6b;
  local_37 = 0x38;
  local_36 = 0x31;
  local_35 = 0x74;
  printf("* ");
  __isoc99_scanf(&DAT_00400a82,local_28);
  printf("[%s]\n",local_28);
  local_14 = strcmp(local_28,local_10);
  if (local_14 != 0) {
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  printf("** ");
  __isoc99_scanf(&DAT_00400a82,local_28);
  __s2 = (char *)FUN_0040078d(0x14);
  iVar1 = strcmp(local_28,__s2);
  if (iVar1 == 0) {
    FUN_00400978(&local_48);
  }
  return;
}
```
I cleaned up and renamed key variables and function calls, and removed unused declarations for clarity:
```c
void Main(void)

{
  int second_correct_key;
  char *second_key;
  undefined initial_flag_value;
  char user_input [20];
  int correct_key;
  char *secret_key;
  
  secret_key = "SuperSeKretKey";
  local_48 = 0x41;
  printf("* ");
  __isoc99_scanf(&DAT_00400a82,user_input);
  printf("[%s]\n",user_input);
  correct_key = strcmp(user_input,secret_key);
  if (correct_key != 0) {
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  printf("** ");
  __isoc99_scanf(&DAT_00400a82,user_input);
  second_key = (char *)build_second_key(0x14);
  second_correct_key = strcmp(user_input,second_key);
  if (second_correct_key != 0) {
    print_flag(&initial_flag_value);
  }
  return;
}
```
As expected the first `strcmp` is a simple compare to the hardcoded secret_key, but the second one relies on a key built from a function `build_second_key` shown below:
```c
void * build_second_key(int param_1)

{
  int random_number;
  time_t time_since_epoch;
  void *second_key;
  int i;
  
  time_since_epoch = time((time_t *)0x0);
  seed = seed + 1;
  srand(seed + (int)time_since_epoch * param_1);
  second_key = malloc((long)(param_1 + 1));
  if (second_key != (void *)0x0) {
    for (i = 0; i < param_1; i = i + 1) {
      random_number = rand();
      *(char *)((long)i + (long)second_key) = (char)(random_number % 0x5e) + '!';
    }
    *(undefined *)((long)second_key + (long)param_1) = 0;
    return second_key;
  }
                    /* WARNING: Subroutine does not return */
  exit(1);
}
```
The function, while intimidating at first due to my poor C knowledge, turned out to be rather simple to decode. The `seed` value initially confused me, but it is just a hardcoded value found at `017DA710h`:
```
                             seed                                            XREF[3]:     build_second_key:004007c0 (R) , 
                                                                                          build_second_key:004007c9 (W) , 
                                                                                          build_second_key:004007cf (R)   
        00601074 10  a7  7d  01    undefine   017DA710h
```
Once it returns `second_key`, it passes it to `strcmp` and if it returns 0, it calls the `print_flag` function to build the flag and print it on screen:
```c
void print_flag(byte *param_1)

{
  int i;
  byte *starting_int;
  
  i = 0;
  starting_int = param_1;
  while ((*starting_int != 9 && (i < 0x14))) {
    putchar((int)(char)(*starting_int ^ 9));
    starting_int = starting_int + 1;
    i = i + 1;
  }
  putchar(10);
  return;
}
```
All we need to do now is essentially make sure that the `strcmp` function will always return `0`, so looking at the assembly for that portion we see:
```x86
        00400966 85  c0            TEST       second_correct_key ,second_correct_key
        00400968 74  0c            JNZ        LAB_00400976
        0040096a 48  8d  45  c0    LEA        second_correct_key =>local_48 ,[RBP  + -0x40 ]
        0040096e 48  89  c7        MOV        RDI ,second_correct_key
        00400971 e8  02  00        CALL       print_flag                                       undefined print_flag()
                 00  00
```
The obvious instruction to target is the `JNZ` which jumps if not equal to 0. By patching that to the `JZ` opcode, we can make it jump no matter what we enter:
```
* SuperSeKretKey
[SuperSeKretKey]
** amogus
HTB{flag}
```






























































































































































