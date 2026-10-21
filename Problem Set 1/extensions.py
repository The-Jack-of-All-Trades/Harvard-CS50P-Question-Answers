def main():
    file_name = input("File name: ").strip().lower() # Converts the input to lowercase

    if file_name.endswith(".jpeg") or file_name.endswith(".jpg"): # Checks if the file_name ends with ".jpeg" or ".jpg"
        print("image/jpeg")

    elif file_name.endswith(".gif"): # Checks if the file_name ends with ".gif"
        print("image/gif")

    elif file_name.endswith(".png"): # Checks if the file_name ends with ".png"
        print("image/png")

    elif file_name.endswith(".pdf"): # Checks if the file_name ends with ".pdf"
        print("application/pdf")

    elif file_name.endswith(".txt"): # Checks if the file_name ends with ".txt"
        print("text/plain")

    elif file_name.endswith(".zip"): # Checks if the file_name ends with ".zip"
        print("application/zip")

    else: # Just to catch anything else
        print("application/octet-stream")


main()
