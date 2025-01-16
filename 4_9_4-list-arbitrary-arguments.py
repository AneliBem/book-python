def write_multiple_items(separator, *args):
    print(separator.join(args))

write_multiple_items(". ", "apple", "banana", "chery")
write_multiple_items(", ", "apple", "banana", "chery")
