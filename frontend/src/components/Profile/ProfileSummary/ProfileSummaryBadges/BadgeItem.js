import React, { Component } from 'react';

import classes from './BadgeItem.module.css'

class BadgeItem extends Component {
  render() {
    console.log(this.props);
    return (
      <div className={classes.BadgeItemContainer}>
        <div className={classes.BadgeItemImage}>
          <img src="https://steamcommunity-a.akamaihd.net/public/images/badges/01_community/community03_80.png" alt="badge"/>
        </div>
        <div className={classes.BadgeItemInfo}>
          <div>
            <span className={classes.BadgeItemTitle}>{this.props.info.description}</span>
            <span className={classes.BadgeItemSubtitle}>{this.props.info.subtitle}</span>
          </div>
          <span className={classes.BadgeItemXp}>{this.props.info.xp}</span>
          <span className={classes.BadgeItemUnlocked}>{this.props.info.unlocked}</span>
        </div>
      </div>
    );
  }
}

export default BadgeItem;