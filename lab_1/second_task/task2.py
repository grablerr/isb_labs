from work_with_json_file import read_path_file
from alphabet import path, key
from freq_analysis import get_text


def decoding(text: str, key_dict: dict) -> str:
    try:
        decrypted_text = "".join(key_dict.get(char, char) for char in text)
        return decrypted_text
    except Exception as e:
        print(f"An error occurred during text decryption: {e}")
        return ""


def main() -> None:
    try:
        json_data = read_path_file(path)
        if json_data:
            folder_path = json_data.get("folder", "")
            input_file = json_data.get("input", "")
            output_file = json_data.get("output", "")

            input_file_path = f"{folder_path}/{input_file}"
            output_file_path = f"{folder_path}/{output_file}"

            text = get_text(input_file_path)
            if text:
                decrypted_text = decoding(text, key)
                if decrypted_text:
                    print(decrypted_text)
                    with open(output_file_path, "w", encoding="utf-8") as file:
                        file.write(decrypted_text)
                        print(f"Decrypted text saved to '{output_file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()