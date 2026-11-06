def is_empty(text):
    cleaned = text.strip()

    if cleaned == "":
        return True

    print("Checking completed")
    return False


print(is_empty("   "))
print(is_empty("Hello, World!"))
