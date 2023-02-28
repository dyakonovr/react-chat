import generateSocialIcon from '../../../functions/generateSocialIcon';
import classes from './Header.module.scss'

function Header({ userObject }) {
  return (
    <div className={classes.wrapper}>
      <div className={classes.image}>
        <img src={`data:image/jpeg;base64,${userObject.avatar}`} alt={userObject.name} />
      </div>
      <a target="_blank" href={userObject.userLink} className={classes.name}>{userObject.name}</a>
      <span className={classes.icon} style={{ 'backgroundImage': `url("${generateSocialIcon(userObject.from)}")` }}></span>
    </div>
  );
};

export default Header;