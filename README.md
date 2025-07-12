# Student Management Module

A comprehensive Odoo 16 module for managing students and courses with advanced features including access control, website integration, and automated workflows.

## Features

### Models
- **Student Model** (`student.student`)
  - Auto-generated student IDs (STU0001, STU0002, etc.)
  - Personal information management
  - Profile photo support
  - Course enrollment tracking
  - State management (Draft → Confirmed → Graduated)
  - Email uniqueness validation
  - Birth date validation (must be in the past)

- **Course Model** (`student.course`)
  - Course information management
  - Unique course codes
  - Student enrollment tracking
  - Smart buttons for navigation

### Access Control
- **Student Manager Group**: Full CRUD access to all records
- **Student User Group**: Read-only access
- Public read access for website display

### User Interface
- Modern form and list views
- Smart buttons showing related records count
- State-based workflow buttons
- Profile photo display
- Course enrollment management

### Website Integration
- Public route `/students` displaying confirmed students
- Course-based filtering
- Responsive design with Bootstrap
- Profile photo display
- Course badges

### Business Logic
- Automatic student ID generation using sequences
- State workflow management
- Data validation constraints
- Many2many relationships between students and courses

## Installation

1. Copy the module to your Odoo addons directory
2. Update the apps list in Odoo
3. Install the "Student Management" module
4. Assign users to the "Student Manager" group for full access

## Usage

### Managing Students
1. Go to Student Management → Students
2. Create new students with required information
3. Use workflow buttons to change student states
4. Enroll students in courses using the Courses tab

### Managing Courses
1. Go to Student Management → Courses
2. Create courses with unique codes
3. View enrolled students using smart buttons
4. Manage course descriptions and details

### Website Display
- Visit `/students` to see public student directory
- Filter by course using the dropdown
- Only confirmed students are displayed

## Technical Details

### Dependencies
- `base`: Core Odoo functionality
- `website`: Website framework for public pages

### File Structure
```
student_management/
├── __init__.py
├── __manifest__.py
├── README.md
├── controllers/
│   ├── __init__.py
│   └── main.py
├── data/
│   └── sequence.xml
├── models/
│   ├── __init__.py
│   ├── course.py
│   └── student.py
├── security/
│   ├── ir.model.access.csv
│   └── security.xml
├── templates/
│   └── website_templates.xml
└── views/
    ├── course_views.xml
    ├── menu.xml
    └── student_views.xml
```

### Key Features Implementation
- **Sequential IDs**: Using `ir.sequence` with prefix "STU" and 4-digit padding
- **Constraints**: Python constraints for email uniqueness and birth date validation
- **Access Control**: Groups and record rules for proper security
- **Website**: HTTP controller with QWeb templates for public display
- **Smart Buttons**: Statistical buttons showing related record counts

## Author
Kyle Sin Lynn

## Version
16.0.1.0.0

## License
This module is licensed under the AGPL License.