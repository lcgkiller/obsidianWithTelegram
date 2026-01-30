import os
import datetime
from config import OBSIDIAN_VAULT_PATH, DAILY_NOTE_FOLDER, DAILY_NOTE_FORMAT

def get_daily_note_path():
    """Calculates the absolute path for today's daily note."""
    today = datetime.datetime.now()
    filename = today.strftime(DAILY_NOTE_FORMAT)
    
    # Construct folder path
    folder_path = OBSIDIAN_VAULT_PATH
    if DAILY_NOTE_FOLDER:
        folder_path = os.path.join(OBSIDIAN_VAULT_PATH, DAILY_NOTE_FOLDER)
    
    return os.path.join(folder_path, filename), folder_path

def ensure_daily_note_exists(file_path, folder_path):
    """Creates the daily note file and folder if they don't exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# Daily Note: {datetime.datetime.now().strftime('%Y-%m-%d')}\n\n")

def add_todo_to_daily_note(todo_text):
    """Appends a todo item under the ## TODO section in the daily note."""
    file_path, folder_path = get_daily_note_path()
    
    try:
        ensure_daily_note_exists(file_path, folder_path)
        
        # Read existing content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        todo_line = f"- [ ] {todo_text}"
        
        # Look for ## TODO section (case insensitive)
        import re
        todo_pattern = re.compile(r'^(##텔레그램에서 추가된 \s*TODO\s*)$', re.IGNORECASE | re.MULTILINE)
        match = todo_pattern.search(content)
        
        if match:
            # Found ## TODO section, insert after it
            insert_pos = match.end()
            
            # Find the next heading (## or #) to know where this section ends
            next_heading = re.search(r'^#', content[insert_pos:], re.MULTILINE)
            
            if next_heading:
                # Insert before the next heading
                section_end = insert_pos + next_heading.start()
                new_content = content[:section_end].rstrip() + f"\n{todo_line}\n\n" + content[section_end:]
            else:
                # No next heading, insert at section and keep rest
                new_content = content[:insert_pos] + f"\n{todo_line}" + content[insert_pos:]
        else:
            # No ## TODO section found, create one at the end
            if not content.endswith('\n'):
                content += '\n'
            new_content = content + f"\n## 텔레그램에서 추가된 TODO\n{todo_line}\n"
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Added to {file_path}: {todo_text}")
        return True, f"Added: {todo_text}"
    except Exception as e:
        print(f"Error updating Obsidian: {e}")
        return False, str(e)

