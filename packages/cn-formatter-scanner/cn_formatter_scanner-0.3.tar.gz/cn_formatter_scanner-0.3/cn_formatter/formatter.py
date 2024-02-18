import re
from typing import List
import hashlib

class CNFormatter:
    
    def __remove_duplicate_words(self,input_string: str) -> str:
            """
            Function to remove duplicate words from a string.

            Args:
            input_string (str): The string from which to remove duplicate words.

            Returns:
            str: A string with duplicate words removed.
            """
            # Splitting the input string into words
            words = input_string.split()

            # Using a set to remove duplicates. This will also preserve the order of words.
            unique_words = []
            seen_words = set()
            for word in words:
                if word not in seen_words:
                    unique_words.append(word)
                    seen_words.add(word)

            # Joining the unique words back into a string
            return ' '.join(unique_words)



    def __remove_words(self, input_string: str) -> str:
        """
        Remove specified words from the input string.

        Args:
        input_string (str): The input string.

        Returns:
        str: String with specified words removed.
        """
        # Construct a regular expression pattern to match the words to remove
        words_to_remove = r'\b(?:st|saint|sg clean|sgclean|city centre|an ihg|chse certified)\b'
        replaced_string = re.sub(words_to_remove, '', input_string, flags=re.IGNORECASE)
        return replaced_string


    def __words_to_remove(self, input_string: str) -> str:
        """
        Remove specified words from the input string.

        Args:
        input_string (str): The input string.

        Returns:
        str: String with specified words removed.
        """
        extended_words = {"apartments"}
        words_to_remove = {"the", "an", "and", "am", "at", "is", "are", "was", "were", "be", "being", "been",
                           "have", "has", "had", "do", "does", "did",
                           "will", "would", "shall", "should", "can", "could", "may", "might", "must", "ought",
                           "a", "its", 'hotels', 'hotel', 'house', 'houses', 'resorts', 'resort',
                           'villas', 'villa', 'hostels', 'hostel', 'suites', 'suite',
                           'residences', 'residence', 'residencia', 'residence', 'perfect', 'charming', 'of',
                           'with', 'near', 'ihg', "st", "saint"}
        words_to_remove = words_to_remove.union(extended_words)
        cleaned_text = ' '.join([word for word in input_string.split() if word.lower() not in words_to_remove])
        return cleaned_text.lower()

    def __remove_location_data(self, text_string: str, location_data_list: List[str]) -> str:
        """
        Remove specified location data from the input string.

        Args:
        text_string (str): The input string.
        location_data_list (List[str]): List of location data to be removed.

        Returns:
        str: String with specified location data removed.
        """
        for location_data in location_data_list:
            text_string = text_string.replace(location_data, "")
        return text_string

    def __replace_diacritic(self, input_string: str) -> str:
        """
        Replace diacritic characters with their ASCII counterparts.

        Args:
        input_string (str): The input string.

        Returns:
        str: String with diacritic characters replaced.
        """
        mapping = {"À": "a", "Á": "a", "Â": "a", "Ã": "a", "Ä": "a", "Å": "a", "Æ": "a", "Ç": "c", "È": "e",
                    "É": "e", "Ê": "e", "Ë": "e", "Ì": "i", "Í": "i", "Î": "i", "Ï": "i", "Ð": "D", "Ñ": "n", "Ò": "o",
                    "Ó": "o", "Ô": "o", "Õ": "o", "Ö": "o", "Ø": "o", "Ù": "u", "Ú": "u", "Û": "u", "Ü": "u", "Ý": "y",
                    "Þ": "p", "ß": "s", "à": "a", "á": "a", "â": "a", "ã": "a", "ä": "a", "å": "a", "æ": "a", "ç": "c",
                    "è": "e", "é": "e", "ê": "e", "ë": "e", "ì": "i", "í": "i", "î": "i", "ï": "i", "ð": "e", "ñ": "n",
                    "ò": "o", "ó": "o", "ô": "o", "õ": "o", "ö": "o", "ø": "o", "ù": "u", "ú": "u", "û": "u", "ü": "u",
                    "ý": "y", "þ": "p", "ÿ": "y", "Ā": "a", "ā": "a", "Ă": "a", "ă": "a", "Ą": "a", "ą": "a", "Ć": "c",
                    "ć": "c", "Ĉ": "c", "ĉ": "c", "Ċ": "c", "ċ": "c", "Č": "c", "č": "c", "Ď": "d", "ď": "d", "Đ": "d",
                    "đ": "d", "Ē": "e", "ē": "e", "Ĕ": "e", "ĕ": "e", "Ė": "e", "ė": "e", "Ę": "e", "ę": "e", "Ě": "e",
                    "ě": "e", "Ĝ": "g", "ĝ": "g", "Ğ": "g", "ğ": "g", "Ġ": "g", "ġ": "g", "Ģ": "g", "ģ": "g", "Ĥ": "h",
                    "ĥ": "h", "Ħ": "h", "ħ": "h", "Ĩ": "i", "ĩ": "i", "Ī": "i", "ī": "i", "Ĭ": "i", "ĭ": "i", "Į": "i",
                    "į": "i", "İ": "i", "ı": "i", "Ĳ": "i", "ĳ": "i", "Ĵ": "j", "ĵ": "j", "Ķ": "k", "ķ": "k", "ĸ": "k",
                    "Ĺ": "l", "ĺ": "l", "Ļ": "l", "ļ": "l", "Ľ": "l", "ľ": "l", "Ŀ": "l", "ŀ": "l", "Ł": "l", "ł": "l",
                    "Ń": "n", "ń": "n", "Ņ": "n", "ņ": "n", "Ň": "n", "ň": "n", "ŉ": "n", "Ŋ": "n", "ŋ": "n", "Ō": "o",
                    "ō": "o", "Ŏ": "o", "ŏ": "o", "Ő": "o", "ő": "o", "Œ": "o", "œ": "o", "Ŕ": "r", "ŕ": "r", "Ŗ": "r",
                    "ŗ": "r", "Ř": "r", "ř": "r", "Ś": "s", "ś": "s", "Ŝ": "s", "ŝ": "s", "Ş": "s", "ş": "s", "Š": "s",
                    "š": "s", "Ţ": "t", "ţ": "t", "Ť": "t", "ť": "t", "Ŧ": "t", "ŧ": "t", "Ũ": "u", "ũ": "u", "Ū": "u",
                    "ū": "u", "Ŭ": "u", "ŭ": "u", "Ů": "u", "ů": "u", "Ű": "u", "ű": "u", "Ų": "u", "ų": "u", "Ŵ": "w",
                    "ŵ": "w", "Ŷ": "y", "ŷ": "y", "Ÿ": "y", "Ź": "z", "ź": "z", "Ż": "z", "ż": "z", "Ž": "z", "ž": "z",
                    "ſ": "s","ệ":"e","ƒ":"f","Ẹ":"E","$":"S"}
        replaced_string = ''.join(mapping.get(char, char) for char in input_string)
        return replaced_string.lower()

    def __clean_text(self, input_string: str) -> str:
        """
        Clean the input string by replacing diacritic characters and removing special characters.

        Args:
        input_string (str): The input string.

        Returns:
        str: Cleaned string.
        """
        try:
            text_normalized = self.__replace_diacritic(input_string)
            text = re.sub(r'[^a-zA-Z0-9\s]', '', text_normalized.lower())
            return text
        except Exception as e:
            print(f"Error in clean_text: {e}")
            return ""

    def __text_formatter(self, input_string: str, city: str, state: str, country: str) -> str:
        """
        Format the input text by cleaning, removing location data, and specific words.

        Args:
        input_string (str): The input string.
        city (str): City name.
        state (str): State name.
        country (str): Country name.

        Returns:
        str: Formatted text.
        """
        try:
            text = self.__clean_text(input_string)
            cleaned_city = self.__clean_text(city)
            cleaned_state = self.__clean_text(state)
            cleaned_country = self.__clean_text(country)
            locations_to_remove = [cleaned_city, cleaned_state, cleaned_country]
            text = self.__remove_location_data(text, locations_to_remove)
            replaced_articles = self.__words_to_remove(text)
            replaced_articles = self.__remove_words(replaced_articles)
            cleaned_text = replaced_articles.replace("apartments", "apartment")
            remove_duplicate_words_in_title = self.__remove_duplicate_words(cleaned_text)
            final_text = remove_duplicate_words_in_title.replace(" ", "")
            return final_text
        except Exception as e:
            print(f"Error in text_formatter: {e}")
            return ""
        
    def __only_clear(self, input_string: str, city: str, state: str, country: str) -> str:
        """
        Format the input text by cleaning, removing location data, and specific words.

        Args:
        input_string (str): The input string.
        city (str): City name.
        state (str): State name.
        country (str): Country name.

        Returns:
        str: Formatted text.
        """
        try:
            text = self.__clean_text(input_string)
            cleaned_city = self.__clean_text(city)
            cleaned_state = self.__clean_text(state)
            cleaned_country = self.__clean_text(country)
            locations_to_remove = [cleaned_city, cleaned_state, cleaned_country]
            text = self.__remove_location_data(text, locations_to_remove)
            final_text = text.replace(" ", "")
            return final_text
        except Exception as e:
            print(f"Error in text_formatter: {e}")
            return ""

    def title_formatter(self, title: str, city: str, state: str, country: str) -> str:
        """
        Format the title by applying the text formatter.

        Args:
        title (str): The title string.
        city (str): City name.
        state (str): State name.
        country (str): Country name.

        Returns:
        str: Formatted title.
        """
        formatted_list = self.__text_formatter(title, city, state, country)
        
        if formatted_list == '':
            formatted_list = self.__only_clear(title, city, state, country)

        return formatted_list
    
    def get_property_key(self, title: str, city: str, state: str, country: str) -> str:
        """
        Get the property by applying the text formatter and return the md5.

        Args:
        title (str): Formated title string.
        city (str): City name.
        state (str): State name.
        country (str): Country name.

        Returns:
        str: MD5 property key.
        """
        property_attributes = title+city+state+country
        property_key =  hashlib.md5(property_attributes.encode()).hexdigest()
        return property_key

