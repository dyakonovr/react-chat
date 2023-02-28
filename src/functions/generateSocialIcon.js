import iconTg from '../assets/icons-tg.svg';
import iconInst from '../assets/icon-inst.svg';
import iconWhatsapp from '../assets/icon-whatsapp.svg';
import iconVk from '../assets/icon-vk.svg';

export default function generateSocialIcon(from) {
  return from === "tg" ? iconTg : from === "vk" ? iconVk : from === "wa" ? iconWhatsapp : iconInst;
}