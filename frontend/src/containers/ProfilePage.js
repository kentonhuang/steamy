import React, { Component } from 'react'
import { withRouter } from 'react-router-dom'

import ProfileSummary from '../components/Profile/ProfileSummary/ProfileSummary';

class ProfilePage extends Component {
  render() {
      console.log(this.props.location);
    return (
      <React.Fragment>
        <ProfileSummary profile={this.props.location.state.profile}/>
      </React.Fragment>
    )
  }
}

export default withRouter(ProfilePage);