import classes from './Preloader.module.scss'
import { useSelector } from 'react-redux';
import { useEffect } from 'react';
import { setTransition } from '../../store/reducers/ActionCreators';
import { store } from '../../store/store';

const Preloader = () => {
  const { preloaderIsVisible, currentClass } = useSelector(state => state.preloaderReducer);

  useEffect(() => {
    if (preloaderIsVisible) { // После некоторого времени добавляю анимацию для прелоадера. Иначе он "мигает" при смене чата
      setTimeout(() => { store.dispatch(setTransition(classes.transition)) }, 200);
    }
  }, [preloaderIsVisible]);

  return (
    <div id="preloader" className={currentClass}><div className={classes.icon}></div></div>
  );
};

export default Preloader;