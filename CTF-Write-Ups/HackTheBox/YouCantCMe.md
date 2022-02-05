# You Cant C Me Writeup
## Materials
- auth (x86 ELF Executable)
## Steps:

We start off with a another x86 ELF binary called auth. When executed, it displays a message saying "Welcome!", and then allows the user to input something.
Inputting anything results in a message saying "I said, you can't c me". Opening it in Ghidra reveals a program with a few functions, but only one is really important:
```c
undefined4 FUN_00401160(void)

{
  int iVar1;
  undefined8 local_48;
  undefined8 local_40;
  undefined4 local_38;
  char *local_30;
  undefined8 local_28;
  undefined8 local_20;
  undefined4 local_18;
  undefined local_14;
  int local_10;
  undefined4 local_c;
  
  local_c = 0;
  local_10 = 0;
  printf("Welcome!\n");
  local_28 = 0x5f73695f73696874;
  local_20 = 0x737361705f656874;
  local_18 = 0x64726f77;
  local_14 = 0;
  local_30 = (char *)malloc(0x15);
  local_48 = 0x5517696626265e6d;
  local_40 = 0x555a275a556b266f;
  local_38 = 0x29635559;
  for (local_10 = 0; local_10 < 0x14; local_10 = local_10 + 1) {
    *(char *)((long)&local_28 + (long)local_10) = *(char *)((long)&local_48 + (long)local_10) + '\n'
    ;
  }
  fgets(local_30,0x15,stdin);
  iVar1 = strcmp((char *)&local_28,local_30);
  if (iVar1 == 0) {
    printf("HTB{%s}\n",local_30);
  }
  else {
    printf("I said, you can\'t c me!\n");
  }
  return local_c;
}
```
After cleaning it up:
```c
undefined4 main(void)

{
  int is_correct_key;
  longlong local_48;
  longlong local_40;
  undefined4 local_38;
  char *user_input;
  longlong pointer_to_key;
  longlong local_20;
  undefined4 local_18;
  undefined local_14;
  int i;
  undefined4 local_c;
  
  local_c = 0;
  i = 0;
  printf("Welcome!\n");
  pointer_to_key = 0x5f73695f73696874;
  local_20 = 0x737361705f656874;
  local_18 = 0x64726f77;
  local_14 = 0;
  user_input = (char *)malloc(0x15);
  local_48 = 0x5517696626265e6d;
  local_40 = 0x555a275a556b266f;
  local_38 = 0x29635559;
  for (i = 0; i < 0x14; i = i + 1) {
    *(char *)((long)&pointer_to_key + (long)i) = *(char *)((long)&local_48 + (long)i) + '\n';
  }
  fgets(user_input,0x15,stdin);
  is_correct_key = strcmp((char *)&pointer_to_key,user_input);
  if (is_correct_key == 0) {
    printf("HTB{%s}\n",user_input);
  }
  else {
    printf("I said, you can\'t c me!\n");
  }
  return local_c;
}
```
Now unlike the previous challenge in this track, BabyRE, this isn't a simple case of searching for an exposed string. 
We are, however, ultimately still focusing on a `strcmp()` call. 
My first try was to simply patch the `CMP` instruction that compares `is_correct_key` to `0x0` to compare to `0x1`, thus effectively making it accept any incorrect input (Patching the following `JZ` instruction to `JNZ` would have a similar effect on the code flow).
This was, admittedly, a little stupid as I failed to realize that following `printf()` function prints the user's input and NOT the flag. I got a little stuck at this point, knowing what change I needed to make in the disassembled c code (`printf("HTB{%s}\n",user_input);` -> `printf("HTB{%s}\n",(char *)&pointer_to_key);`), but not knowing how to translate that into patching the assembly.
I wanted to simply change the parameter in the `printf()` to `(char *)&pointer_to_key`, but couldnt figure out how. In the process, I found a simpler solution: patching the `CALL` instruction of the `strcmp()` function to instead call `printf()`:
```c
  is_correct_key = printf((char *)&pointer_to_key,user_input);
  if (is_correct_key == 0) {
    printf("HTB{%s}\n",user_input);
  }
```
This results in the program printing out the flag (*******************) and then the message for an incorrect input:
```
[mili@Omen-15 YouCantCMe]$ YouCantCMe ./auth_patched_6                             11:23PM
Welcome!
1234567890input
*******************I said, you can't c me!
```

Overall, I think that I need to get much more familar with C going through this track, as I dont know if cheap tricks like this will work on more complicated challenges.
