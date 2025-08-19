import time
tries = 4
print("You have 4 attempts.\nYour password is a 4 digit PIN.\nEach attempts reduce your try by one.\nAttempt to enter more or less than 4 digits PIN or other form of characters combination will cut try by 2.\nUpon a failed entry. A physical confirmation and clearance will be mandatory to proceed.")
while tries > 0:
    pwd = input("Enter your password: ").strip()
    if pwd.isdigit() and len(pwd) == 4:
        if pwd == "4321":
            print("✅Access granted. Lockbox opened.")
            break
        else:
            tries -= 1
            print(f"⚠️Invalid PIN. You have {tries} tries left.\nHint: Enter 4 digits PIN.\nPlease wait 3 seconds before retrying... " if tries > 1 else f"⚠️Invalid PIN. This is your last try.\nHint: Enter 4 digits PIN.\nPlease wait 3 seconds before retrying... " if tries == 1 else f"⚠️Too many failed attempts detecte.\nSecurity alert initiating..." )
            time.sleep(3)
    else:
        penalty = 2
        tries = max(0, tries - penalty)
        if tries > 0:
            print(f"Invalid PIN combination.\n Attempting more or less than 4 digits PIN or including non-numeric character twice will result in automatic lockdown.")
            print(f"You have {tries} tries left.\nPlease wait 3 seconds before retrying..."if tries > 1 else f"\nThis is your last try.\nPlease wait 3 seconds before retrying...")
        else:
            print(f"⚠️You have exhausted your try limit.\nSecurity alert initiating...")
        time.sleep(3)          
else:
    print("🔐Lockbox disabled. Security alert sent.\nPlease visit a nearby service center for physical clearance.")  