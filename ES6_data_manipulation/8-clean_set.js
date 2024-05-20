export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }

  const filtrValues = Array.from(set).filter((value) => value.startsWith(startString));
  const cleanValues = filtrValues.map((value) => {
    if (value.startsWith(startString)) {
      return value.replace(new RegExp(`${startString}`), '');
    }
    return value;
  });
  return cleanValues.join('-');
}
