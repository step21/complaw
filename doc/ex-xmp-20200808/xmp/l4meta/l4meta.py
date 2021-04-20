import exif
import terminal

def process():
    parser, args = terminal.arguments()
    
    # Silent or verbose
    if args.verbose:
        print(vars(args))
    elif args.silent:
        pass
    
    with exif.MetaTool() as e:
        is_read = args.mode == 0
        if is_read:
            return e.read(args.file, args.type)
        else:
            return e.write_single(
                    in_file = args.input,
                    out_file = args.output,
                    meta_file = args.meta
            )

def main():
    print(process())

if __name__ == '__main__':
    main()
