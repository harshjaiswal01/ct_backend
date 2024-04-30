def mood_response(mood):
        # Implement your response logic here
        if mood == 'happy':
                return "Congratulations on achieving Happiness!!!"
        elif mood == 'sad':
                return "Awww...Please feel happy soon. Goodluck!!!"
        elif mood == 'okay':
                return "Lets hope you feel better soon!"
        else:
                return "Invalid Response"