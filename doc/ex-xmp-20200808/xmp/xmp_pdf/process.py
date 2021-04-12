import os
import exif
import json
import shutil
import yaml
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
            return e.read(args.file[0].name, output_format = args.type)
        else:
            return write(e, args)

def write(e, args):
    result = ''

    # Copy over file
    shutil.copy2(args.input[0].name, args.output[0].name)

    # Process metafile
    metadata = e.read_metadata(args.meta[0].name)
    meta_flat = e.stringify(metadata)

    new_file = 'new2.json'
    with open(new_file, 'w+') as file:
        file.write(meta_flat + "\n")
        result = e.write(args.output[0].name, metafile = new_file)

    return result
