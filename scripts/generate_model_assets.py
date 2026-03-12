import os

def generate_dummy_model(path, size_mb):
    """Generates a dummy binary file of a specific size to simulate AI model weights."""
    with open(path, "wb") as f:
        f.write(os.urandom(size_mb * 1024 * 1024))
    print(f"Generated {path} ({size_mb} MB)")

if __name__ == "__main__":
    generate_dummy_model("assets/models/language_model.bin", 15)
    generate_dummy_model("assets/models/complaint_classifier.bin", 45)
    generate_dummy_model("assets/models/embedding_model.bin", 30)
    generate_dummy_model("assets/models/response_model.bin", 60)
