class ReportGenerator:
    def generate(self, student):
        return f"Report for {student.name}"

class PDFReportGenerator(ReportGenerator):
    def generate(self, student):
        return f"PDF Report for {student.name}"

class HTMLReportGenerator(ReportGenerator):
    def generate(self, student):
        return f"HTML Report for {student.name}"
