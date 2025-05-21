from datetime import date
from odoo import api, fields, models

class BookDetails(models.Model):
    _name = "book.details"
    _description = "Book Details"
    
    title = fields.Char(string="Title")
    author = fields.Char(string="Author")
    publisher = fields.Char(string="Publisher")
    published_date = fields.Date(string="Published Date")
    book_age = fields.Integer(
                string="Book Age",
                compute="_compute_book_age",
                store=True,
                readonly=True)
    genre = fields.Selection(string="Genre", selection=[('fiction', 'Fiction'), ('non-fiction', 'Non-Fiction')])
    
    
    @api.depends("published_date")
    def _compute_book_age(self):
            for record in self:
                if record.published_date:
                    today = date.today()
                    record.book_age = today.year - record.published_date.year - (
                        (today.month, today.day) < (record.published_date.month, record.published_date.day)
                    )
                else:
                    record.book_age = 0
        