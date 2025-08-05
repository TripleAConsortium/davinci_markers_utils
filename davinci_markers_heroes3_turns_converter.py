import sys
import re

const_color_text = 'C:ResolveColor'
const_color_len = len(const_color_text)

def get_date_components(days):
    if days < 1:
        return None
    
    month = (days - 1) // 28 + 1
    remaining_days = (days - 1) % 28 + 1
    
    week = (remaining_days - 1) // 7 + 1
    day = (remaining_days - 1) % 7 + 1
    
    return f'{month}{week}{day}'

def count_colors(filename, verbose=False, initial_yellow=0, initial_lemon=0, initial_sand=0, initial_cocoa=0):
    yellow_count = initial_yellow
    blue_count = 0
    red_count = 0
    green_count = 0
    fuchsia_count = 0
    mint_count = 0
    lemon_count = initial_lemon
    sand_count = initial_sand
    cocoa_count = initial_cocoa
    result = ""
    
    with open(filename, 'r') as file:
        content = file.read()
        
        matches = re.finditer(const_color_text, content)
        
        for match in matches:
            start_pos = match.start()
            
            back_start = max(0, start_pos - 52)
            back_text = content[back_start:back_start + 8]
            
            forward_text = content[start_pos + const_color_len:start_pos + const_color_len + 6]

            if forward_text.startswith('Yellow'):
                yellow_count += 1
                result += f'{back_text} - {get_date_components(yellow_count)}\n'
                if verbose:
                    print(f"Found Yellow: 52 chars back='{back_text}', forward='{forward_text}'")
            elif forward_text.startswith('Lemon'):
                lemon_count += 1
                result += f'{back_text} - {get_date_components(lemon_count)}\n'
                if verbose:
                    print(f"Found Lemon: 52 chars back='{back_text}', forward='{forward_text}'")
            elif forward_text.startswith('Sand'):
                sand_count += 1
                result += f'{back_text} - {get_date_components(sand_count)}\n'
                if verbose:
                    print(f"Found Sand: 52 chars back='{back_text}', forward='{forward_text}'")
            elif forward_text.startswith('Cocoa'):
                cocoa_count += 1
                result += f'{back_text} - {get_date_components(cocoa_count)}\n'
                if verbose:
                    print(f"Found Cocoa: 52 chars back='{back_text}', forward='{forward_text}'")
            elif forward_text.startswith('Blue'):
                blue_count += 1
                custom_text = content[start_pos + const_color_len + 8:start_pos + 100].split(' |D:')[0]
                result += f'{back_text} - {custom_text}\n'
                if verbose:
                    print(f"Found Blue: 52 chars back='{back_text}', forward='{forward_text}'")
            elif forward_text.startswith('Red'):
                red_count += 1
                result += f'{back_text} - Звук пропал\n'
                if verbose:
                    print(f"Found Red: 52 chars back='{back_text}', forward='{forward_text}'")
            elif forward_text.startswith('Green'):
                green_count += 1
                result += f'{back_text} - Звук вернулся\n'
                if verbose:
                    print(f"Found Green: 52 chars back='{back_text}', forward='{forward_text}'")
            elif forward_text.startswith('Fuchsi'):
                fuchsia_count += 1
                result += f'{back_text} - Финалочка\n'
                if verbose:
                    print(f"Found Fuchsia: 52 chars back='{back_text}', forward='{forward_text}'")
            elif forward_text.startswith('Mint'):
                mint_count += 1
                result += f'{back_text} - Микрофончик\n'
                if verbose:
                    print(f"Found Mint: 52 chars back='{back_text}', forward='{forward_text}'")
    
    if verbose:
        print("\nCounts:")
        print(f"Yellow: {yellow_count} (initial: {initial_yellow})")
        print(f"Lemon: {lemon_count} (initial: {initial_lemon})")
        print(f"Sand: {sand_count} (initial: {initial_sand})")
        print(f"Cocoa: {cocoa_count} (initial: {initial_cocoa})")
        print(f"Blue: {blue_count}")
        print(f"Red: {red_count}")
        print(f"Green: {green_count}")
        print(f"Fuchsia: {fuchsia_count}")
        print(f"Mint: {mint_count}")
        print("\nResult:")

    print(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename> [--verbose] [--yellow N] [--lemon M] [--sand S] [--cocoa C]")
        sys.exit(1)
    
    verbose = False
    initial_yellow = 0
    initial_lemon = 0
    initial_sand = 0
    initial_cocoa = 0
    
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == '--verbose':
            verbose = True
            i += 1
        elif sys.argv[i] == '--yellow' and i + 1 < len(sys.argv):
            try:
                initial_yellow = int(sys.argv[i+1])
                i += 2
            except ValueError:
                print("Error: --yellow requires an integer value")
                sys.exit(1)
        elif sys.argv[i] == '--lemon' and i + 1 < len(sys.argv):
            try:
                initial_lemon = int(sys.argv[i+1])
                i += 2
            except ValueError:
                print("Error: --lemon requires an integer value")
                sys.exit(1)
        elif sys.argv[i] == '--sand' and i + 1 < len(sys.argv):
            try:
                initial_sand = int(sys.argv[i+1])
                i += 2
            except ValueError:
                print("Error: --sand requires an integer value")
                sys.exit(1)
        elif sys.argv[i] == '--cocoa' and i + 1 < len(sys.argv):
            try:
                initial_cocoa = int(sys.argv[i+1])
                i += 2
            except ValueError:
                print("Error: --cocoa requires an integer value")
                sys.exit(1)
        else:
            print(f"Error: Unknown argument {sys.argv[i]}")
            sys.exit(1)
    
    count_colors(sys.argv[1], verbose, initial_yellow, initial_lemon, initial_sand, initial_cocoa)
