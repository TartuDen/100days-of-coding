alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = ""

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
# ugvafy


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
def get_conditions():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift>11 or shift <=0:
    print("Too large number or invalid number. The number should be between 1 and 10, try again")
    get_conditions()
  return(direction, text, shift)

def encrypt_func(enc_dec_message, txt_,shft):
  enc_dec_txt=""
  if enc_dec_message.lower()=="encode":
    for ch in txt_:
      if ch in alphabet:
        if alphabet.index(ch)<shft:
          code_idx=(len(alphabet)) - (shft-alphabet.index(ch))
        else:
          code_idx=alphabet.index(ch)-shft
        print(code_idx, alphabet[code_idx])
        enc_dec_txt+=alphabet[code_idx]
      else:
        enc_dec_txt+=ch
  else:
    for ch in txt_:
      if ch in alphabet:
        if (alphabet.index(ch)+shft)>len(alphabet)-1:
          code_idx=(shft+alphabet.index(ch))-len(alphabet)
        else:
          code_idx=alphabet.index(ch)+shft
        # print(code_idx, alphabet[code_idx])
        enc_dec_txt+=alphabet[code_idx]
      else:
        enc_dec_txt+=ch
  return(enc_dec_txt)
again="y"
while again.lower()=="y":
  start=get_conditions()
  print(encrypt_func(start[0],start[1],start[2]))
  again=input("Again? Y / N ")
