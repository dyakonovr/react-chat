export default function generateLink(id, social) {
  if (social === "vk") return `https://vk.com/id${id}`;
  if (social === "wa") return `https://api.whatsapp.com/send?phone=${id.slice(0, id.lastIndexOf('@'))}`
  if (social === "tg") return `https://t.me/${id}`
}