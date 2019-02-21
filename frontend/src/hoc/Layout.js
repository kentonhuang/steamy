import React, { Component } from 'react'
import axios from 'axios'

import { Route, Redirect, withRouter } from 'react-router-dom'

import classes from './Layout.module.css';
import SearchPage from '../containers/SearchPage';
import ProfilePage from '../containers/ProfilePage';

class Layout extends Component {

    state = {
        profile: {}
    }

    updateProfile = (id) => {
        let url = 'http://0.0.0.0:8000/api/steamuser/' + id
        axios.get(url)
            .then(res => {
                const profile = res.data;
                this.setState({profile})

                this.props.history.push({
                    pathname: `/profile/${id}`,
                    state: {profile}
                })
            })
    }

  render() {
      console.log(this.state.profile);
    return (
        <main className={classes.Wrapper}>
            <Route path="/" exact component={() => <SearchPage updateProfile={this.updateProfile} />} />
            <Route path="/profile/:id" component={() => <ProfilePage />} />
        </main>
    )
  }
}

export default withRouter(Layout);