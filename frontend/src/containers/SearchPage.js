import React, { Component } from 'react'

import SearchBox from '../components/SearchBox/SearchBox';

export default class SearchPage extends Component {

    state = {
        text: '',
    }

    handleChange = (event) => {
        this.setState({
            text: event.target.value
        })
    }

    handleSubmit = (event) => {
        event.preventDefault();
        this.props.updateProfile(this.state.text);
    }

  render() {
    return (
      <React.Fragment>
        <SearchBox submit={this.handleSubmit} change={this.handleChange} text={this.state.text}/>
      </React.Fragment>
    )
  }
}
