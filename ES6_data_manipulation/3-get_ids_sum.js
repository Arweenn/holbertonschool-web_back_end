export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  return students.reduce((sum, students) => sum + students.id, 0);
}
