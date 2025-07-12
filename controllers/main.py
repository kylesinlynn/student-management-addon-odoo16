from odoo import http
from odoo.http import request


class StudentController(http.Controller):

    @http.route('/students', type='http', auth='public', website=True)
    def students_list(self, course_filter=None, **kwargs):
        domain = [('state', '=', 'confirmed')]
        
        # Get all courses for the filter dropdown
        courses = request.env['student.course'].sudo().search([])
        
        # Apply course filter if provided
        if course_filter:
            try:
                course_id = int(course_filter)
                domain.append(('course_ids', 'in', [course_id]))
            except (ValueError, TypeError):
                pass
        
        # Get confirmed students
        students = request.env['student.student'].sudo().search(domain)
        
        return request.render('student_management.students_list', {
            'students': students,
            'courses': courses,
            'selected_course': course_filter,
        })
