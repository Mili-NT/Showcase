# Baby RE Writeup
## Materials
- baby (x86 ELF Executable)
## Steps:

We are given a simple x86 ELF executable, which when ran prompts us to enter a key. If an incorrect key is entered, the program closes.
From this program structure, I can guess that we are looking for a simple `strcmp()` instruction. Opening the file in Ghidra shows that its very simple, with all the action happening in the `main` function:
```c
undefined8 main(void)

{
  int iVar1;
  undefined8 local_48;
  undefined8 local_40;
  undefined4 local_38;
  undefined2 local_34;
  char local_28 [24];
  char *local_10;
  
  local_10 = "Dont run `strings` on this challenge, that is not the way!!!!";
  puts("Insert key: ");
  fgets(local_28,0x14,stdin);
  iVar1 = strcmp(local_28,"abcde122313\n");
  if (iVar1 == 0) {
    local_48 = 0x594234427b425448;
    local_40 = 0x3448545f5633525f;
    local_38 = 0x455f5354;
    local_34 = 0x7d5a;
    puts((char *)&local_48);
  }
  else {
    puts("Try again later.");
  }
  return 0;
}
```
After cleaning it up a bit:
```c
undefined8 main(void)

{
  int is_correct_key;
  long long pointer_to_flag;
  long long local_40;
  undefined4 local_38;
  undefined2 local_34;
  char key_input [24];
  char *announcement;
  
  announcement = "Dont run `strings` on this challenge, that is not the way!!!!";
  puts("Insert key: ");
  fgets(key_input,0x14,stdin);
  is_correct_key = strcmp(key_input,"abcde122313\n");
  if (is_correct_key == 0) {
    pointer_to_flag = 0x594234427b425448;
    local_40 = 0x3448545f5633525f;
    local_38 = 0x455f5354;
    local_34 = 0x7d5a;
    puts((char *)&pointer_to_flag);
  }
  else {
    puts("Try again later.");
  }
  return 0;
}
```
As I thought, this is a simple `strcmp()` comparing key_input to the string "abcde122313\n" and if the `strcmp()` function returns 0 it will cast the `pointer_to_flag` to the char type, giving us the flag.
