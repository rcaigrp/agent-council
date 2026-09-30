# Verify what classes actually exist in our implementation files
import inspect
import analysis
import recommendations
import ui_components

class_names = []
for name, obj in inspect.getmembers(analysis, inspect.isclass):
    class_names.append(name)
    print(f"Analysis module has class: {name}")
    
print("\nClasses found in analysis.py:")
for name in class_names:
    print(f"  - {name}")

# Check recommendations
rec_class_names = []
for name, obj in inspect.getmembers(recommendations, inspect.isclass):
    rec_class_names.append(name)
    print(f"Recommendations module has class: {name}")
    
print("\nClasses found in recommendations.py:")
for name in rec_class_names:
    print(f"  - {name}")

# Check ui_components
ui_class_names = []
for name, obj in inspect.getmembers(ui_components, inspect.isclass):
    ui_class_names.append(name)
    print(f"UI Components module has class: {name}")
    
print("\nClasses found in ui_components.py:")
for name in ui_class_names:
    print(f"  - {name}")