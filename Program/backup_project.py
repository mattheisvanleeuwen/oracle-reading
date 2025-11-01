"""
Backup System for The Oracle - Insight Project
Creates versioned, timestamped backups with restore instructions.
"""

import os
import shutil
from datetime import datetime
from pathlib import Path
import re


# Exclusion patterns
EXCLUDE_DIRS = {
    '__pycache__',
    '.git',
    'node_modules',
    '.venv',
    'venv',
    'env',
    'Backups',  # Don't backup the backups folder
}

EXCLUDE_PATTERNS = {
    r'^Backup_v\d+.*',  # Don't backup old backup folders in root
}

EXCLUDE_EXTENSIONS = {
    '.pyc',
    '.pyo',
    '.log',
    '.tmp',
}


def should_exclude(path, base_path):
    """Check if a path should be excluded from backup."""
    rel_path = os.path.relpath(path, base_path)
    
    # Check if it's an excluded directory
    path_parts = Path(rel_path).parts
    if any(part in EXCLUDE_DIRS for part in path_parts):
        return True
    
    # Check if it matches excluded patterns (for root level items)
    if os.path.dirname(rel_path) == '.':
        for pattern in EXCLUDE_PATTERNS:
            if re.match(pattern, os.path.basename(path)):
                return True
    
    # Check if it has an excluded extension
    if os.path.splitext(path)[1] in EXCLUDE_EXTENSIONS:
        return True
    
    return False


def get_next_version():
    """Scan the Backups folder to determine the next version number."""
    backups_dir = Path('Backups')
    if not backups_dir.exists():
        return 1
    
    max_version = 0
    for item in backups_dir.iterdir():
        if item.is_dir() and item.name.startswith('Backup_v'):
            # Extract version number from folder name
            match = re.match(r'Backup_v(\d+)', item.name)
            if match:
                version = int(match.group(1))
                max_version = max(max_version, version)
    
    return max_version + 1


def create_restore_instructions(backup_path, version, timestamp, backed_up_items):
    """Generate restore instructions for the backup."""
    restore_md = f"""# Restore Instructions for Backup v{version}

**Backup Created:** {timestamp}  
**Backup Location:** `{backup_path}`

## What's Included

This backup contains a complete snapshot of The Oracle - Insight project at the time of backup.

### Backed Up Items:
"""
    
    # List all backed up items
    for item in sorted(backed_up_items):
        item_type = "[DIR]" if os.path.isdir(os.path.join(backup_path, item)) else "[FILE]"
        restore_md += f"- {item_type} `{item}`\n"
    
    restore_md += """
### Excluded Items:
The following items were excluded from the backup:
- `__pycache__/` directories
- `.git/` directory
- `node_modules/` directory
- Virtual environments (`venv/`, `.venv/`, `env/`)
- Compiled Python files (`*.pyc`, `*.pyo`)
- Log files (`*.log`)
- Temporary files (`*.tmp`)
- The `Backups/` folder itself
- Other backup folders in the root

## How to Restore

### Option 1: Full Restore (Replace Current Project)

1. **Backup your current work** (if needed):
   - Make sure you've saved any work you want to keep from the current project state

2. **Navigate to your project location**:
   ```
   cd "G:\\My Drive\\Mattheis van Leeuwen Holding BV\\Documenten\\CursorAI\\The Oracle - Insight"
   ```

3. **Delete current project files** (except the Backups folder):
   - Manually delete files and folders you want to replace
   - OR move them to a temporary location

4. **Copy all files from this backup**:
   - Copy all contents from this backup folder to the project root
   - Do NOT copy this `RESTORE_INSTRUCTIONS.md` file to the root

5. **Reinstall dependencies**:
   ```batch
   install_dependencies.bat
   ```
   OR manually:
   ```batch
   pip install -r requirements.txt
   ```

### Option 2: Selective Restore (Cherry-pick Files)

1. Browse this backup folder
2. Copy only the specific files/folders you need
3. Paste them into your current project, replacing as needed

### Option 3: Create New Project from Backup

1. **Create a new project folder**:
   ```
   mkdir "The Oracle - Insight (Restored)"
   cd "The Oracle - Insight (Restored)"
   ```

2. **Copy all files from this backup** into the new folder

3. **Install dependencies**:
   ```batch
   pip install -r requirements.txt
   ```

4. **Test the application**:
   ```batch
   python Program\oracle_app.py
   ```

## Verification Steps

After restoring, verify the installation:

1. **Check Python dependencies**:
   ```batch
   pip list
   ```

2. **Run the application**:
   ```batch
   python Program\oracle_app.py
   ```

3. **Check for missing files**: Compare with this backup to ensure all needed files are present

## Important Notes

- This backup is a folder copy (uncompressed) for easy browsing and selective restoration
- Dependencies listed in `requirements.txt` need to be reinstalled after restoration
- API keys and environment variables (if any) need to be reconfigured
- If you had a virtual environment, you'll need to recreate it

## Support

For questions or issues with restoration, refer to:
- `Documentation\01_README_Application_Overview.md` - Main application documentation
- `Documentation\02_GUIDE_Deployment.md` - Deployment instructions
- `requirements.txt` - Python dependencies list

---
*Backup created by backup_project.py on {timestamp}*
"""
    
    # Write the restore instructions
    restore_path = os.path.join(backup_path, 'RESTORE_INSTRUCTIONS.md')
    with open(restore_path, 'w', encoding='utf-8') as f:
        f.write(restore_md)
    
    print(f"✓ Created restore instructions: {restore_path}")


def create_backup():
    """Create a new versioned backup of the project."""
    # Get project root (parent directory if running from Program folder)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir) if os.path.basename(script_dir) == 'Program' else script_dir
    
    # Change to project root for backup operations
    original_dir = os.getcwd()
    os.chdir(project_root)
    
    # Get next version number
    version = get_next_version()
    
    # Create timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Create backup folder name
    backup_name = f"Backup_v{version}_{timestamp}"
    backup_path = os.path.join('Backups', backup_name)
    
    print(f"\n{'='*60}")
    print(f"Creating Backup v{version}")
    print(f"{'='*60}")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Backup Location: {backup_path}")
    print(f"{'='*60}\n")
    
    # Create backup directory
    os.makedirs(backup_path, exist_ok=True)
    
    # Track what was backed up
    backed_up_items = []
    
    # Copy files and directories
    items = os.listdir(project_root)
    total_items = len(items)
    processed = 0
    
    for item in items:
        source_path = os.path.join(project_root, item)
        
        # Skip excluded items
        if should_exclude(source_path, project_root):
            print(f"⊗ Skipping: {item}")
            processed += 1
            continue
        
        dest_path = os.path.join(backup_path, item)
        
        try:
            if os.path.isdir(source_path):
                # Copy directory
                print(f"📁 Copying directory: {item}")
                shutil.copytree(source_path, dest_path, 
                              ignore=lambda dir, files: [
                                  f for f in files 
                                  if should_exclude(os.path.join(dir, f), project_root)
                              ])
            else:
                # Copy file
                print(f"📄 Copying file: {item}")
                shutil.copy2(source_path, dest_path)
            
            backed_up_items.append(item)
        except Exception as e:
            print(f"✗ Error copying {item}: {e}")
        
        processed += 1
    
    # Create restore instructions
    print(f"\n{'='*60}")
    print("Generating restore instructions...")
    print(f"{'='*60}\n")
    create_restore_instructions(backup_path, version, 
                               datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                               backed_up_items)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"✓ BACKUP COMPLETE")
    print(f"{'='*60}")
    print(f"Version: v{version}")
    print(f"Location: {backup_path}")
    print(f"Items backed up: {len(backed_up_items)}")
    print(f"Timestamp: {timestamp}")
    print(f"{'='*60}\n")
    
    # Restore original directory
    os.chdir(original_dir)
    
    return backup_path, version


if __name__ == '__main__':
    try:
        create_backup()
    except Exception as e:
        print(f"\n✗ Backup failed: {e}")
        import traceback
        traceback.print_exc()

