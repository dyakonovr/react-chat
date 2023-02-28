export default function generateDate(date) {
  const currDate = new Date(String(date));

  return `${currDate.getHours() < 10 ? '0' + currDate.getHours() : currDate.getHours()}:${currDate.getMinutes() < 10 ? '0' + currDate.getMinutes() : currDate.getMinutes()}:${currDate.getSeconds() < 10 ? '0' + currDate.getSeconds() : currDate.getSeconds()}, ${currDate.toLocaleDateString("ru-RU")}`
}