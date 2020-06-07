from flask import request, render_template

def home_page(**params):
    if request.method == "GET":
        return render_template('public/main/index.html', **params)

    elif request.method == "POST":
        text_input = request.form.get("text_input")
        rot_number = request.form.get("rot_number")
        rot_number_int = 0
        text_input = text_input.lower()
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        message = "No input was given."

        if text_input and rot_number:
            # validate form input
            character_validation = False
            number_validation = False
            number_bounds_validation = False

            # check if there is only characters from alphabet in the text input
            for character in text_input:
                if character in alphabet:
                    character_validation = True
                else:
                    character_validation = False
                    message = "There was a bad character in your text input."

            # check if number input is indeed integer
            if character_validation:
                try:
                    rot_number_int = int(rot_number)
                    number_validation = True
                except:
                    message = "Enter a number in the number field."

            # check if number is within bounds
            if number_validation:
                if 26 > rot_number_int > 0:
                    number_bounds_validation = True
                else:
                    number_bounds_validation = False
                    message = "Enter a number between 1 and 25."

            # main encryption
            if number_bounds_validation:
                alphabet = "abcdefghijklmnopqrstuvwxyz"
                encrypted = ""

                # for each character in user input, check where in alphabet it is located,
                # save the index and sum with ROT number for encryption. If the index is
                # out of alphabet bounds, subtract by 26 (starts from beginning of alphabet)
                for character in text_input:
                    counter = 0
                    for alphabet_character in alphabet:
                        if alphabet_character == character:
                            index = counter + rot_number_int
                            if index > 25:
                                index = index - 26
                            encrypted += alphabet[index]
                        counter += 1

                message = "Your encrypted text: " + encrypted

        params["message"] = message
        return render_template('public/main/index.html', **params)
