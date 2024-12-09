from mimesis import Person, Address
from mimesis.locales import Locale

# Initialize Mimesis generators for Romania locale
person = Person(Locale.RO)
address = Address(Locale.RO)

# Generate sample personal data
print("Generated Personal Data:")
print("Name:", person.full_name())
print("Email:", person.email())
print("Phone Number:", person.telephone())
print("Street Address:", address.address())
print("City:", address.city())
print("Postal Code:", address.postal_code())

# Generate multiple records
def generate_multiple_records(num_records):
    print("\nGenerating multiple records:")
    for _ in range(num_records):
        print("---")
        print("Name:", person.full_name())
        print("Email:", person.email())
        print("Phone Number:", person.telephone())
        print("Street Address:", address.address())
        print("City:", address.city())
        print("Postal Code:", address.postal_code())

# Generate 5 records as a test
generate_multiple_records(5)