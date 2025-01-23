// Character counter JS:
        /**
         * Select the textarea element.
         */
        const textAreaElement = document.querySelector("#text_field");
        /**
         * Select the character counter element.
         */
        const characterCounterElement = document.querySelector("#character-counter");
        /**
         * Select the element that shows the number of characters typed in the textarea.
         */
        const typedCharactersElement = document.querySelector("#typed-characters");
        /**
         * Define the maximum number of characters allowed.
         */
        const maximumCharacters = 800;
        /**
         * Add a "keyup" event listener on the textarea element.
         */
        if (textAreaElement != null) {
            textAreaElement.addEventListener("keyup", (event) => {
                /**
                 * Count the number of characters typed.
                 */
                const typedCharacters = textAreaElement.value.length;
                /**
                 * Check if the typed characters is more than allowed characters limit.
                 * If yes, then return false.
                 */
                if (typedCharacters > maximumCharacters) {
                    return false;
                }
                /**
                 * Display the number of characters typed.
                 */
                typedCharactersElement.textContent = typedCharacters;
                /**
                 * Change the character counter text colour to "orange" if the typed
                 * characters number is between 400 to 600. If more, then change the colour to "red".
                 */
                if (typedCharacters >= 400 && typedCharacters < 600) {
                    characterCounterElement.classList = "mt-2 text-amber-600";
                } else if (typedCharacters >= 600) {
                    characterCounterElement.classList = "mt-2 text-red-600";
                }
            });
        };