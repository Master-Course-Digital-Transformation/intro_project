class ReportGenerator:
    def generate(self, student):
        return f"Report for {student.name}"

# open closed principle violated: design should be open for extension but closed for modification