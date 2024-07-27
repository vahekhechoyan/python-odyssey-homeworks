# 1
def greet_user(first_name, last_name, message="Hello"):
    full_name = f"{first_name} {last_name}"
    greeting = f"{message}, {full_name}!"
    return greeting


print(greet_user("Jack", "Doe"))
print(greet_user("Jane", "Smith", message="Welcome"))




# 2
def calculate_total_price(*prices, tax_rate=0.05):
    """
    Calculate the total price of items including tax.
    
    :param prices: Positional-only arguments representing the prices of individual items.
    :param tax_rate: Keyword argument for the tax rate, default is 5%.
    :return: Total price including tax.
    """
    subtotal = sum(prices)
    total_price = subtotal * (1 + tax_rate)
    return total_price


print(calculate_total_price(10.0, 20.0, 30.0))  
print(calculate_total_price(10.0, 20.0, 30.0, tax_rate=0.1)) 


# 3
def print_user_profile(first_name, last_name, *, age, city):
    """
    Print the user profile.

    :param first_name: Positional argument for the first name.
    :param last_name: Positional argument for the last name.
    :param age: Keyword-only argument for age.
    :param city: Keyword-only argument for city.
    :return: Formatted user profile string.
    """
    profile = (
        f"User Profile:\n"
        f"Name: {first_name} {last_name}\n"
        f"Age: {age}\n"
        f"City: {city}"
    )
    return profile


print(print_user_profile("John", "Doe", age=30, city="New York"))


# 4
def process_data(data, /, *, operation='sum'):
    """
    Process data with a specified operation.

    :param data: Positional-only argument, list of numbers to process.
    :param operation: Keyword argument for the operation to perform, default is 'sum'.
    :return: Result of the operation.
    """
    if operation == 'sum':
        return sum(data)
    elif operation == 'mean':
        return sum(data) / len(data) if data else 0
    elif operation == 'max':
        return max(data) if data else None
    elif operation == 'min':
        return min(data) if data else None
    else:
        raise ValueError(f"Unsupported operation: {operation}")


print(process_data([1, 2, 3, 4, 5]))  # Default operation 'sum'
print(process_data([1, 2, 3, 4, 5], operation='mean'))
print(process_data([1, 2, 3, 4, 5], operation='max'))
print(process_data([1, 2, 3, 4, 5], operation='min'))



# 5
def display_product_details(**details):
    """
    Display product details.

    :param details: Keyword arguments representing product details.
    :return: Formatted string with product details.
    """
    product_info = "Product Details:\n"
    for key, value in details.items():
        product_info += f"{key.capitalize()}: {value}\n"
    return product_info


product = {
    'name': 'Laptop',
    'brand': 'BrandX',
    'price': 999.99,
    'stock': 50,
    'category': 'Electronics'
}

print(display_product_details(**product))


# 6
def generate_report(title, content, *, author="Anonymous", date="N/A", footer="Thank you for reading."):
    """
    Generate a report with required and optional sections.

    :param title: Positional argument for the report title.
    :param content: Positional argument for the main content of the report.
    :param author: Keyword argument for the author of the report, default is "Anonymous".
    :param date: Keyword argument for the date of the report, default is "N/A".
    :param footer: Keyword argument for the footer of the report, default is "Thank you for reading.".
    :return: Formatted report string.
    """
    report = (
        f"Report Title: {title}\n"
        f"Author: {author}\n"
        f"Date: {date}\n"
        f"\n{content}\n"
        f"\n{footer}"
    )
    return report


title = "Quarterly Financial Summary"
content = "The company's quarterly financial summary shows an increase in revenue by 10% compared to the last quarter."
print(generate_report(title, content))
print(generate_report(title, content, author="John Doe", date="July 2024", footer="For more information, visit our website."))

# 7
def log_messages(severity, *messages, **metadata):
    """
    Log messages with varying levels of severity and optional metadata.

    :param severity: Severity level of the messages.
    :param messages: Arbitrary number of messages to log.
    :param metadata: Keyword arguments for metadata like timestamp, user, etc.
    :return: Formatted log entry string.
    """
    log_entry = f"Severity: {severity}\n"
    for message in messages:
        log_entry += f"Message: {message}\n"
    
    if metadata:
        log_entry += "Metadata:\n"
        for key, value in metadata.items():
            log_entry += f"  {key}: {value}\n"
    
    return log_entry


print(log_messages("ERROR", "File not found", "Unable to open file", timestamp="2024-07-27 14:00:00", user="admin"))
print(log_messages("INFO", "User logged in", user="jdoe", timestamp="2024-07-27 15:30:00"))


# 8
def log_messages(severity, *messages, **metadata):
    """
    Log messages with varying levels of severity and optional metadata.

    :param severity: Severity level of the messages.
    :param messages: Arbitrary number of messages to log.
    :param metadata: Keyword arguments for metadata like timestamp, user, etc.
    :return: Formatted log entry string.
    """
    log_entry = f"Severity: {severity}\n"
    for message in messages:
        log_entry += f"Message: {message}\n"
    
    if metadata:
        log_entry += "Metadata:\n"
        for key, value in metadata.items():
            log_entry += f"  {key}: {value}\n"
    
    return log_entry

print(log_messages("ERROR", "File not found", "Unable to open file", timestamp="2024-07-27 14:00:00", user="admin"))
print(log_messages("INFO", "User logged in", user="jdoe", timestamp="2024-07-27 15:30:00"))

