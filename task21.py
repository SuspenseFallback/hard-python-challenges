sampling_rate = float(input("Enter sampling rate of sound (Hz): "))
resolution = float(input("Enter resolution of sound (bits): "))
length = float(input("Enter length of sound (seconds): "))

size = sampling_rate * length * resolution

print("The file size is:", size, "bits")
