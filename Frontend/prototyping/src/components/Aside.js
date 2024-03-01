function Aside(){
    return (
        <div><>
        {/* aside */}
        <div id="aside" className="app-aside modal nav-dropdown">
          {/* fluid app aside */}
          <div className="left navside dark dk" data-layout="column">
            <div className="navbar no-radius">
              {/* brand */}
              <a className="navbar-brand">
                <div ui-include="'../assets/images/logo.svg'" />
                <img src="../assets/images/logo.png" alt="." className="hide" />
                <span className="hidden-folded inline">Flatkit</span>
              </a>
              {/* / brand */}
            </div>
            <div className="hide-scroll" data-flex="">
              <nav className="scroll nav-light">
                <ul className="nav" ui-nav="">
                  <li className="nav-header hidden-folded">
                    <small className="text-muted">Main</small>
                  </li>
                  <li>
                    <a href="dashboard.html">
                      <span className="nav-icon">
                        <i className="material-icons">
                          
                          <span ui-include="'../assets/images/i_0.svg'" />
                        </i>
                      </span>
                      <span className="nav-text">Dashboard</span>
                    </a>
                  </li>
                  <li>
                    <a>
                      <span className="nav-caret">
                        <i className="fa fa-caret-down" />
                      </span>
                      <span className="nav-label">
                        <b className="label rounded label-sm primary">5</b>
                      </span>
                      <span className="nav-icon">
                        <i className="material-icons">
                          
                          <span ui-include="'../assets/images/i_1.svg'" />
                        </i>
                      </span>
                      <span className="nav-text">Apps</span>
                    </a>
                    <ul className="nav-sub">
                      <li>
                        <a href="inbox.html">
                          <span className="nav-text">Inbox</span>
                        </a>
                      </li>
                      <li>
                        <a href="contact.html">
                          <span className="nav-text">Contacts</span>
                        </a>
                      </li>
                      <li>
                        <a href="calendar.html">
                          <span className="nav-text">Calendar</span>
                        </a>
                      </li>
                    </ul>
                  </li>
                  <li>
                    <a>
                      <span className="nav-caret">
                        <i className="fa fa-caret-down" />
                      </span>
                      <span className="nav-icon">
                        <i className="material-icons">
                          
                          <span ui-include="'../assets/images/i_2.svg'" />
                        </i>
                      </span>
                      <span className="nav-text">Layouts</span>
                    </a>
                    <ul className="nav-sub">
                      <li>
                        <a href="headers.html">
                          <span className="nav-text">Header</span>
                        </a>
                      </li>
                      <li>
                        <a href="asides.html">
                          <span className="nav-text">Aside</span>
                        </a>
                      </li>
                      <li>
                        <a href="footers.html">
                          <span className="nav-text">Footer</span>
                        </a>
                      </li>
                    </ul>
                  </li>
                  <li>
                    <a href="widget.html">
                      <span className="nav-icon">
                        <i className="material-icons">
                          
                          <span ui-include="'../assets/images/i_3.svg'" />
                        </i>
                      </span>
                      <span className="nav-text">Widgets</span>
                    </a>
                  </li>
                  <li className="nav-header hidden-folded">
                    <small className="text-muted">Components</small>
                  </li>
                  <li>
                    <a>
                      <span className="nav-caret">
                        <i className="fa fa-caret-down" />
                      </span>
                      <span className="nav-label">
                        <b className="label label-sm accent">8</b>
                      </span>
                      <span className="nav-icon">
                        <i className="material-icons">
                          
                          <span ui-include="'../assets/images/i_4.svg'" />
                        </i>
                      </span>
                      <span className="nav-text">UI kit</span>
                    </a>
                    <ul className="nav-sub nav-mega nav-mega-3">
                      <li>
                        <a href="arrow.html">
                          <span className="nav-text">Arrow</span>
                        </a>
                      </li>
                      <li>
                        <a href="box.html">
                          <span className="nav-text">Box</span>
                        </a>
                      </li>
                      <li>
                        <a href="button.html">
                          <span className="nav-text">Button</span>
                        </a>
                      </li>
                      <li>
                        <a href="color.html">
                          <span className="nav-text">Color</span>
                        </a>
                      </li>
                      <li>
                        <a href="dropdown.html">
                          <span className="nav-text">Dropdown</span>
                        </a>
                      </li>
                      <li>
                        <a href="grid.html">
                          <span className="nav-text">Grid</span>
                        </a>
                      </li>
                      <li>
                        <a href="icon.html">
                          <span className="nav-text">Icon</span>
                        </a>
                      </li>
                      <li>
                        <a href="label.html">
                          <span className="nav-text">Label</span>
                        </a>
                      </li>
                      <li>
                        <a href="list.html">
                          <span className="nav-text">List Group</span>
                        </a>
                      </li>
                      <li>
                        <a href="modal.html">
                          <span className="nav-text">Modal</span>
                        </a>
                      </li>
                      <li>
                        <a href="nav.html">
                          <span className="nav-text">Nav</span>
                        </a>
                      </li>
                      <li>
                        <a href="progress.html">
                          <span className="nav-text">Progress</span>
                        </a>
                      </li>
                      <li>
                        <a href="social.html">
                          <span className="nav-text">Social</span>
                        </a>
                      </li>
                      <li>
                        <a href="sortable.html">
                          <span className="nav-text">Sortable</span>
                        </a>
                      </li>
                      <li>
                        <a href="streamline.html">
                          <span className="nav-text">Streamline</span>
                        </a>
                      </li>
                      <li>
                        <a href="timeline.html">
                          <span className="nav-text">Timeline</span>
                        </a>
                      </li>
                      <li>
                        <a href="map.vector.html">
                          <span className="nav-text">Vector Map</span>
                        </a>
                      </li>
                    </ul>
                  </li>
                  <li>
                    <a>
                      <span className="nav-caret">
                        <i className="fa fa-caret-down" />
                      </span>
                      <span className="nav-label">
                        <b className="label no-bg">9</b>
                      </span>
                      <span className="nav-icon">
                        <i className="material-icons">
                          
                          <span ui-include="'../assets/images/i_5.svg'" />
                        </i>
                      </span>
                      <span className="nav-text">Pages</span>
                    </a>
                    <ul className="nav-sub nav-mega">
                      <li>
                        <a href="profile.html">
                          <span className="nav-text">Profile</span>
                        </a>
                      </li>
                      <li>
                        <a href="setting.html">
                          <span className="nav-text">Setting</span>
                        </a>
                      </li>
                      <li>
                        <a href="search.html">
                          <span className="nav-text">Search</span>
                        </a>
                      </li>
                      <li>
                        <a href="faq.html">
                          <span className="nav-text">FAQ</span>
                        </a>
                      </li>
                      <li>
                        <a href="gallery.html">
                          <span className="nav-text">Gallery</span>
                        </a>
                      </li>
                      <li>
                        <a href="invoice.html">
                          <span className="nav-text">Invoice</span>
                        </a>
                      </li>
                      <li>
                        <a href="price.html">
                          <span className="nav-text">Price</span>
                        </a>
                      </li>
                      <li>
                        <a href="blank.html">
                          <span className="nav-text">Blank</span>
                        </a>
                      </li>
                      <li>
                        <a href="signin.html">
                          <span className="nav-text">Sign In</span>
                        </a>
                      </li>
                      <li>
                        <a href="signup.html">
                          <span className="nav-text">Sign Up</span>
                        </a>
                      </li>
                      <li>
                        <a href="forgot-password.html">
                          <span className="nav-text">Forgot Password</span>
                        </a>
                      </li>
                      <li>
                        <a href="lockme.html">
                          <span className="nav-text">Lockme Screen</span>
                        </a>
                      </li>
                      <li>
                        <a href="404.html">
                          <span className="nav-text">Error 404</span>
                        </a>
                      </li>
                      <li>
                        <a href="505.html">
                          <span className="nav-text">Error 505</span>
                        </a>
                      </li>
                    </ul>
                  </li>
                  <li>
                    <a>
                      <span className="nav-caret">
                        <i className="fa fa-caret-down" />
                      </span>
                      <span className="nav-icon">
                        <i className="material-icons">
                          
                          <span ui-include="'../assets/images/i_6.svg'" />
                        </i>
                      </span>
                      <span className="nav-text">Form</span>
                    </a>
                    <ul className="nav-sub">
                      <li>
                        <a href="form.layout.html">
                          <span className="nav-text">Form Layout</span>
                        </a>
                      </li>
                      <li>
                        <a href="form.element.html">
                          <span className="nav-text">Form Element</span>
                        </a>
                      </li>
                      <li>
                        <a href="form.validation.html">
                          <span className="nav-text">Form Validation</span>
                        </a>
                      </li>
                      <li>
                        <a href="form.select.html">
                          <span className="nav-text">Select</span>
                        </a>
                      </li>
                      <li>
                        <a href="form.editor.html">
                          <span className="nav-text">Editor</span>
                        </a>
                      </li>
                      <li>
                        <a href="form.picker.html">
                          <span className="nav-text">Picker</span>
                        </a>
                      </li>
                      <li>
                        <a href="form.wizard.html">
                          <span className="nav-text">Wizard</span>
                        </a>
                      </li>
                      <li>
                        <a href="form.dropzone.html" className="no-ajax">
                          <span className="nav-text">File Upload</span>
                        </a>
                      </li>
                    </ul>
                  </li>
                  <li>
                    <a>
                      <span className="nav-caret">
                        <i className="fa fa-caret-down" />
                      </span>
                      <span className="nav-icon">
                        <i className="material-icons">
                          
                          <span ui-include="'../assets/images/i_7.svg'" />
                        </i>
                      </span>
                      <span className="nav-text">Tables</span>
                    </a>
                    <ul className="nav-sub">
                      <li>
                        <a href="static.html">
                          <span className="nav-text">Static table</span>
                        </a>
                      </li>
                      <li>
                        <a href="datatable.html">
                          <span className="nav-text">Datatable</span>
                        </a>
                      </li>
                      <li>
                        <a href="footable.html">
                          <span className="nav-text">Footable</span>
                        </a>
                      </li>
                    </ul>
                  </li>
                  <li>
                    <a>
                      <span className="nav-caret">
                        <i className="fa fa-caret-down" />
                      </span>
                      <span className="nav-label hidden-folded">
                        <b className="label label-sm info">N</b>
                      </span>
                      <span className="nav-icon">
                        <i className="material-icons">
                          
                          <span ui-include="'../assets/images/i_8.svg'" />
                        </i>
                      </span>
                      <span className="nav-text">Charts</span>
                    </a>
                    <ul className="nav-sub">
                      <li>
                        <a href="chart.html">
                          <span className="nav-text">Chart</span>
                        </a>
                      </li>
                      <li>
                        <a>
                          <span className="nav-caret">
                            <i className="fa fa-caret-down" />
                          </span>
                          <span className="nav-text">Echarts</span>
                        </a>
                        <ul className="nav-sub">
                          <li>
                            <a href="echarts-line.html">
                              <span className="nav-text">line</span>
                            </a>
                          </li>
                          <li>
                            <a href="echarts-bar.html">
                              <span className="nav-text">Bar</span>
                            </a>
                          </li>
                          <li>
                            <a href="echarts-pie.html">
                              <span className="nav-text">Pie</span>
                            </a>
                          </li>
                          <li>
                            <a href="echarts-scatter.html">
                              <span className="nav-text">Scatter</span>
                            </a>
                          </li>
                          <li>
                            <a href="echarts-radar-chord.html">
                              <span className="nav-text">Radar &amp; Chord</span>
                            </a>
                          </li>
                          <li>
                            <a href="echarts-gauge-funnel.html">
                              <span className="nav-text">Gauges &amp; Funnel</span>
                            </a>
                          </li>
                          <li>
                            <a href="echarts-map.html">
                              <span className="nav-text">Map</span>
                            </a>
                          </li>
                        </ul>
                      </li>
                    </ul>
                  </li>
                  <li className="nav-header hidden-folded">
                    <small className="text-muted">Help</small>
                  </li>
                  <li className="hidden-folded">
                    <a href="docs.html">
                      <span className="nav-text">Documents</span>
                    </a>
                  </li>
                </ul>
              </nav>
            </div>
            <div className="b-t">
              <div className="nav-fold">
                <a href="profile.html">
                  <span className="pull-left">
                    <img
                      src="../assets/images/a0.jpg"
                      alt="..."
                      className="w-40 img-circle"
                    />
                  </span>
                  <span className="clear hidden-folded p-x">
                    <span className="block _500">Jean Reyes</span>
                    <small className="block text-muted">
                      <i className="fa fa-circle text-success m-r-sm" />
                      online
                    </small>
                  </span>
                </a>
              </div>
            </div>
          </div>
        </div>
        {/* / */}
      </>
      </div>
    )
}

export default Aside;