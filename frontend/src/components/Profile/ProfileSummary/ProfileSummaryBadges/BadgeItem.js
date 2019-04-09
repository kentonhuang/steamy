import React, { Component } from 'react';

import classes from './BadgeItem.module.css'

class BadgeItem extends Component {

  getImage = () => {
    if(this.props.badgeinfo.badgeid > 0) {
      return this.props.info.image
    }
    else {
      if(this.props.badgeinfo.appid) {
        if(this.props.badgeinfo.level > 1) {
          return this.props.info[`image` + this.props.badgeinfo.level]
        }
        else {
          return this.props.info[`image`]
        }
      } 
    }
  }

  render() {
    return (
      <div className={classes.BadgeItemContainer}>
        <div className={classes.BadgeItemImage}>
          <img src={this.getImage()} alt="badge"/>
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