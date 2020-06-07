# Smartninja challenge 2020-5-6
Smartninja coding challenge for 2020-5-6 (Caesar's cipher)

Link to challenge: https://github.com/smartninja/smartninja-challenges/blob/master/monthly-challenges/2020-5-6.md

I created a Caesar's cipher using Flask environment. I used no other Python libraries, just basic Python 3. The app allows you to enter text and number with which you want to encrypt this text (ROT number). The app validates your inputs. Characters used in text input have to be in English alphabet.
After the app validates your input, it goes through your text input and checks, where your characters are located in the alphabet. After it locates the character it sums it with ROT number and it returns your encrypted text. If the index goes out of bounds of alphabet, it substracts the index by 26. That way it starts from beginning.
If you know the ROT number you can also decrypt the message by substracting from your encrypted message.
