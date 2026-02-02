"""
Professional To-Do List Application
A console-based task management system with full CRUD operations.

Author: Senior Python Engineer
License: MIT
"""

from typing import List, Dict, Optional


def display_menu() -> None:
    """Display the main menu options to the user."""
    print("\n" + "=" * 50)
    print("           TO-DO LIST APPLICATION")
    print("=" * 50)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit")
    print("=" * 50)


def add_task(tasks: List[Dict[str, any]]) -> None:
    """
    
    
Args:
tasks: List of task dictionaries containing 'name' and 'completed' keys.
    
Returns:
None
"""
    try:
        task_name = input("\nEnter task name: ").strip()
        
        if not task_name:
            print("❌ Error: Task name cannot be empty.")
            return
        
        task = {
            "name": task_name,
           "completed": False
        }
        
        tasks.append(task)
        print(f"✅ Task '{task_name}' added successfully!")
        
    except Exception as e:
        print(f"❌ Unexpected error while adding task: {e}")


def view_tasks(tasks: List[Dict[str, any]]) -> None:
    """
Display all tasks with their current status.
    
    Args:
    tasks: List of task dictionaries containing 'name' and 'completed' keys.
    
    Returns:
None
"""
    try:
        if not tasks:
            print("\n📋 No tasks found. Your to-do list is empty!")
            return
        
        print("\n" + "-" * 50)
        print("                  YOUR TASKS")
        print("-" * 50)
        
        for idx, task in enumerate(tasks, start=1):
            status = "[✓]" if task["completed"] else "[ ]"
            task_name = task["name"]
            print(f"{idx}. {status} {task_name}")
        
        print("-" * 50)
        
    except Exception as e:
        print(f"❌ Unexpected error while viewing tasks: {e}")


def update_task_status(tasks: List[Dict[str, any]]) -> None:
    """
 Update the completion status of an existing task.
    
Args:
tasks: List of task dictionaries containing 'name' and 'completed' keys.
    
Returns:
None
"""
    try:
        if not tasks:
            print("\n📋 No tasks available to update.")
            return
        
        view_tasks(tasks)
        
        task_number = input("\nEnter task number to update: ").strip()
        
        if not task_number.isdigit():
            print("❌ Error: Please enter a valid number.")
            return
        
        task_idx = int(task_number) - 1
        
        if task_idx < 0 or task_idx >= len(tasks):
            print(f"❌ Error: Task number must be between 1 and {len(tasks)}.")
            return
        
        # Toggle completion status
        tasks[task_idx]["completed"] = not tasks[task_idx]["completed"]
        
        status = "completed" if tasks[task_idx]["completed"] else "incomplete"
        print(f"✅ Task '{tasks[task_idx]['name']}' marked as {status}!")
        
    except ValueError:
        print("❌ Error: Invalid input. Please enter a number.")
    except Exception as e:
        print(f"❌ Unexpected error while updating task: {e}")


def delete_task(tasks: List[Dict[str, any]]) -> None:
    """
Delete a task from the to-do list.
    
Args:
tasks: List of task dictionaries containing 'name' and 'completed' keys.
    
Returns:
None 
"""
    try:
        if not tasks:
            print("\n📋 No tasks available to delete.")
            return
        
        view_tasks(tasks)
        
        task_number = input("\nEnter task number to delete: ").strip()
        
        if not task_number.isdigit():
            print("❌ Error: Please enter a valid number.")
            return
        
        task_idx = int(task_number) - 1
        
        if task_idx < 0 or task_idx >= len(tasks):
            print(f"❌ Error: Task number must be between 1 and {len(tasks)}.")
            return
        
        deleted_task = tasks.pop(task_idx)
        print(f"✅ Task '{deleted_task['name']}' deleted successfully!")
        
    except ValueError:
        print("❌ Error: Invalid input. Please enter a number.")
    except Exception as e:
        print(f"❌ Unexpected error while deleting task: {e}")


def main() -> None:
    """
 Main application entry point.
Manages the application loop and user interactions.
    
    
Returns:
None    
"""
    tasks: List[Dict[str, any]] = []
    print("\n🎯 Welcome to the Professional To-Do List Application!")
    
    while True:
        try:
            display_menu()
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                update_task_status(tasks)
            elif choice == "4":
                delete_task(tasks)
            elif choice == "5":
                print("\n👋 Thank you for using the To-Do List Application!")
                print("Goodbye!\n")
                break
            else:
                print("❌ Invalid choice. Please select a number between 1 and 5.")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Application interrupted by user.")
            print("👋 Goodbye!\n")
            break
        except Exception as e:
            print(f"❌ Unexpected error in main loop: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()