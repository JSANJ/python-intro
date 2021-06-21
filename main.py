import argparse

def main(in_path,out_path):
    print(f"Reading file from {in_path}")
    
    print("Do something here...")
    
    print(f"Save to {out_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Description of your program")
    parser.add_argument("in_path", help="Path of file to read")
    parser.add_argument("out_path", help="Path of file to save to")
    
    # Read arguments from the command line
    args = parser.parse_args()
    main(args.in_path, args.out_path)
