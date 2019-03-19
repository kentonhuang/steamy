import React, { Component } from 'react';
import axios from 'axios';

import classes from './ProfileSummaryBadges.module.css'

import BadgeItem from './BadgeItem';

class ProfileSummaryBadges extends Component {

  state = {
    loading: true,
    badges: {}
  }

  componentDidMount() {
    let url = 'http://localhost:8000/api/badges/' + this.props.id64
    axios.get(url)
      .then(res => {
        const badges = res.data;
        this.setState({badges})
        this.setState({loading: false})
      })
  }

  renderItems = () => {
    if(!this.state.loading) {
      let badges = this.state.badges.map((item, i) => {
        return <BadgeItem key={i} info={item} badgeinfo={this.props.badges}/>
      })
      return badges
    }
  }

  render() {
    return (
      <div className={classes.ProfileSummaryBadges}>
        {this.renderItems()}
      </div>
    );
  }
}

export default ProfileSummaryBadges;