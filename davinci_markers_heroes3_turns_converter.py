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

def count_colors(filename, verbose=False):
    yellow_count = 0
    blue_count = 0
    red_count = 0
    green_count = 0
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
    
    if verbose:
        print("\nCounts:")
        print(f"Yellow: {yellow_count}")
        print(f"Blue: {blue_count}")
        print(f"Red: {red_count}")
        print(f"Green: {green_count}")
        print("\nResult:")

    print(result)

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python script.py <filename> [--verbose]")
        sys.exit(1)
    
    verbose = False
    if len(sys.argv) == 3 and sys.argv[2] == '--verbose':
        verbose = True
    
    count_colors(sys.argv[1], verbose)
