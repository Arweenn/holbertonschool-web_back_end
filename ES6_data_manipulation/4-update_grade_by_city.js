export default function updateStudentGradeByCity(studentsList, city, newGrades) {
  return studentsList
    .filter((student) => student.location === city)
    .map((student) => {
      const grades = newGrades.find((grade) => grade.studentId === student.id);
      if (grades) {
        return { ...student, grade: grades.grade };
      }
      return { ...student, grade: 'N/A' };
    });
}
