import React from 'react';
import { Link } from 'react-router-dom';
import LogoSVG from '../images/logo.svg';
import I_0 from '../images/i_0.svg';
import I_1 from '../images/i_1.svg';
import I_2 from '../images/i_2.svg';
import I_3 from '../images/i_3.svg';
import I_4 from '../images/i_4.svg';
import I_5 from '../images/i_5.svg';
import I_6 from '../images/i_6.svg';
import I_7 from '../images/i_7.svg';
import I_8 from '../images/i_8.svg';

const MainLayout = ({ children }) => {
  return (
    <div>
        <div className="app" id="app">
    <div id="aside" className="app-aside modal nav-dropdown">
      <div className="left navside dark dk" data-layout="column">
        <div className="navbar no-radius">
          <a className="navbar-brand">
            <LogoSVG className="logo-svg" />
            <img src="/assets/images/logo.png" alt="." className="hide" />
            <span className="hidden-folded inline">Flatkit</span>
          </a>
        </div>
        <div className="hide-scroll" data-flex>
          <nav className="scroll nav-light">
            <ul className="nav" ui-nav>
              <li className="nav-header hidden-folded">
                <small className="text-muted">Main</small>
              </li>
              <li>
                <Link to="dashboard.html">
                  <span className="nav-icon">
                    <i className="material-icons">&#xe3fc;
                    <I_0 className="i_0" />
                    </i>
                  </span>
                  <span className="nav-text">Dashboard</span>
                </Link>
              </li>
              <li>
                <a>
                  <span className="nav-caret">
                    <i className="fa fa-caret-down"></i>
                  </span>
                  <span className="nav-label">
                    <b className="label rounded label-sm primary">5</b>
                  </span>
                  <span className="nav-icon">
                    <i className="material-icons">&#xe5c3;
                        <I_1 className="i_1" />
                    </i>
                  </span> 
                  <span className="nav-text">Apps</span>
                </a>
                <ul className="nav-sub">
                  <li>
                  <Link to="inbox.html">
                      <span className="nav-text">Inbox</span>
                    </Link>
                  </li>
                  <li>
                  <Link to="contact.html">
                      <span className="nav-text">Contacts</span>
                    </Link>
                  </li>
                  <li>
                  <Link to="calendar.html">
                      <span className="nav-text">Calendar</span>
                    </Link>
                  </li>
                </ul>
              </li>
              <li>
                <a>
                  <span className="nav-caret">
                    <i className="fa fa-caret-down"></i>
                  </span>
                  <span className="nav-icon">
                    <i className="material-icons">&#xe8f0;
                        <I_2 className="i_2" />
                    </i>
                  </span>
                  <span className="nav-text">Layouts</span>
                </a>
                <ul className="nav-sub">
                  <li>
                    <Link to="headers.html">
                      <span className="nav-text">Header</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="asides.html">
                      <span className="nav-text">Aside</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="footers.html">
                      <span className="nav-text">Footer</span>
                    </Link>
                  </li>
                </ul>
              </li>
              <li>
                <Link to="widget.html">
                  <span className="nav-icon">
                    <i className="material-icons">&#xe8d2;
                        <I_3 className="i_3" />
                    </i>
                  </span>
                  <span className="nav-text">Widgets</span>
                </Link>
              </li>
              <li className="nav-header hidden-folded">
                <small className="text-muted">Components</small>
              </li>
              <li>
                <a>
                  <span className="nav-caret">
                    <i className="fa fa-caret-down"></i>
                  </span>
                  <span className="nav-label">
                    <b className="label label-sm accent">8</b>
                  </span>
                  <span className="nav-icon">
                    <i className="material-icons">&#xe429;
                        <I_4 className="i_4" />
                    </i>
                  </span>
                  <span className="nav-text">UI kit</span>
                </a>
                <ul className="nav-sub nav-mega nav-mega-3">
                  <li>
                    <Link to="arrow.html">
                      <span className="nav-text">Arrow</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="box.html">
                      <span className="nav-text">Box</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="button.html">
                      <span className="nav-text">Button</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="color.html">
                      <span className="nav-text">Color</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="dropdown.html">
                      <span className="nav-text">Dropdown</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="grid.html">
                      <span className="nav-text">Grid</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="icon.html">
                      <span className="nav-text">Icon</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="label.html">
                      <span className="nav-text">Label</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="list.html">
                      <span className="nav-text">List Group</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="modal.html">
                      <span className="nav-text">Modal</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="nav.html">
                      <span className="nav-text">Nav</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="progress.html">
                      <span className="nav-text">Progress</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="social.html">
                      <span className="nav-text">Social</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="sortable.html">
                      <span className="nav-text">Sortable</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="streamline.html">
                      <span className="nav-text">Streamline</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="timeline.html">
                      <span className="nav-text">Timeline</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="map.vector.html">
                      <span className="nav-text">Vector Map</span>
                    </Link>
                  </li>
                </ul>
              </li>
              <li>
                <a>
                  <span className="nav-caret">
                    <i className="fa fa-caret-down"></i>
                  </span>
                  <span className="nav-label"><b className="label no-bg">9</b></span>
                  <span className="nav-icon">
                    <i className="material-icons">&#xe3e8;
                        <I_5 className="i_5" /> 
                    </i>
                  </span>
                  <span className="nav-text">Pages</span>
                </a>
                <ul className="nav-sub nav-mega">
                  <li>
                    <Link to="profile.html">
                      <span className="nav-text">Profile</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="setting.html">
                      <span className="nav-text">Setting</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="search.html">
                      <span className="nav-text">Search</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="faq.html">
                      <span className="nav-text">FAQ</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="gallery.html">
                      <span className="nav-text">Gallery</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="invoice.html">
                      <span className="nav-text">Invoice</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="price.html">
                      <span className="nav-text">Price</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="blank.html">
                      <span className="nav-text">Blank</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="signin.html">
                      <span className="nav-text">Sign In</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="signup.html">
                      <span className="nav-text">Sign Up</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="forgot-password.html">
                      <span className="nav-text">Forgot Password</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="lockme.html">
                      <span className="nav-text">Lockme Screen</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="404.html">
                      <span className="nav-text">Error 404</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="505.html">
                      <span className="nav-text">Error 505</span>
                    </Link>
                  </li>
                </ul>
              </li>
              <li>
                <a>
                  <span className="nav-caret">
                    <i className="fa fa-caret-down"></i>
                  </span>
                  <span className="nav-icon">
                    <i className="material-icons">&#xe39e;
                        <I_6 className="i_6" />
                    </i>
                  </span>
                  <span className="nav-text">Form</span>
                </a>
                <ul className="nav-sub">
                  <li>
                    <Link to="form.layout.html">
                      <span className="nav-text">Form Layout</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="form.element.html">
                      <span className="nav-text">Form Element</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="form.validation.html">
                      <span className="nav-text">Form Validation</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="form.select.html">
                      <span className="nav-text">Select</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="form.editor.html">
                      <span className="nav-text">Editor</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="form.picker.html">
                      <span className="nav-text">Picker</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="form.wizard.html">
                      <span className="nav-text">Wizard</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="form.dropzone.html" className="no-ajax">
                      <span className="nav-text">File Upload</span>
                    </Link>
                  </li>
                </ul>
              </li>
              <li>
                <a>
                  <span className="nav-caret">
                    <i className="fa fa-caret-down"></i>
                  </span>
                  <span className="nav-icon">
                    <i className="material-icons">&#xe896;
                        <I_7 className="i_7" />
                    </i>
                  </span>
                  <span className="nav-text">Tables</span>
                </a>
                <ul className="nav-sub">
                  <li>
                    <Link to="static.html">
                      <span className="nav-text">Static table</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="datatable.html">
                      <span className="nav-text">Datatable</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="footable.html">
                      <span className="nav-text">Footable</span>
                    </Link>
                  </li>
                </ul>
              </li>
              <li>
                <a>
                  <span className="nav-caret">
                    <i className="fa fa-caret-down"></i>
                  </span>
                  <span className="nav-label hidden-folded">
                    <b className="label label-sm info">N</b>
                  </span>
                  <span className="nav-icon">
                    <i className="material-icons">&#xe1b8;
                        <I_8 className="i_8" />
                    </i>
                  </span>
                  <span className="nav-text">Charts</span>
                </a>
                <ul className="nav-sub">
                  <li>
                    <Link to="chart.html">
                      <span className="nav-text">Chart</span>
                    </Link>
                  </li>
                  <li>
                    <a>
                      <span className="nav-caret">
                        <i className="fa fa-caret-down"></i>
                      </span>
                      <span className="nav-text">Echarts</span>
                    </a>
                    <ul className="nav-sub">
                      <li>
                        <Link to="echarts-line.html">
                          <span className="nav-text">line</span>
                        </Link>
                      </li>
                      <li>
                        <Link to="echarts-bar.html">
                          <span className="nav-text">Bar</span>
                        </Link>
                      </li>
                      <li>
                        <Link to="echarts-pie.html">
                          <span className="nav-text">Pie</span>
                        </Link>
                      </li>
                      <li>
                        <Link to="echarts-scatter.html">
                          <span className="nav-text">Scatter</span>
                        </Link>
                      </li>
                      <li>
                        <Link to="echarts-radar-chord.html">
                          <span className="nav-text">Radar &amp; Chord</span>
                        </Link>
                      </li>
                      <li>
                        <Link to="echarts-gauge-funnel.html">
                          <span className="nav-text">Gauges &amp; Funnel</span>
                        </Link>
                      </li>
                      <li>
                        <Link to="echarts-map.html">
                          <span className="nav-text">Map</span>
                        </Link>
                      </li>
                    </ul>
                  </li>
                </ul>
              </li>
              <li className="nav-header hidden-folded">
                <small className="text-muted">Help</small>
              </li>
              <li className="hidden-folded">
                <Link to="docs.html">
                  <span className="nav-text">Documents</span>
                </Link>
              </li>
            </ul>
          </nav>
        </div>
        <div className="b-t">
          <div className="nav-fold">
            <Link to="profile.html">
              <span className="pull-left">
                <img src="../images/a0.jpg" alt="..." className="w-40 img-circle" />
              </span>
              <span className="clear hidden-folded p-x">
                <span className="block _500">Jean Reyes</span>
                <small className="block text-muted"><i className="fa fa-circle text-success m-r-sm"></i>online</small>
              </span>
            </Link>
          </div>
        </div>
      </div>
    </div>
    <div id="content" className="app-content box-shadow-z0" role="main">
      <div className="app-header white box-shadow">
        <div className="navbar navbar-toggleable-sm flex-row align-items-center">
          <a data-toggle="modal" data-target="#aside" className="hidden-lg-up mr-3">
            <i className="material-icons">&#xe5d2;</i>
          </a>
          <div className="mb-0 h5 no-wrap" ng-bind="$state.current.data.title" id="pageTitle"></div>
          <div className="collapse navbar-collapse" id="collapse">
            <ul className="nav navbar-nav mr-auto">
              <li className="nav-item dropdown">
                <a className="nav-link" href data-toggle="dropdown">
                  <i className="fa fa-fw fa-plus text-muted"></i>
                  <span>New</span>
                </a>
                <div ui-include="/views/blocks/dropdown.new.html'"></div>
              </li>
            </ul>
            <div ui-include="/views/blocks/navbar.form.html'"></div>
          </div>
          <ul className="nav navbar-nav ml-auto flex-row">
            <li className="nav-item dropdown pos-stc-xs">
              <a className="nav-link mr-2" href data-toggle="dropdown">
                <i className="material-icons">&#xe7f5;</i>
                <span className="label label-sm up warn">3</span>
              </a>
              <div ui-include="/views/blocks/dropdown.notification.html'"></div>
            </li>
            <li className="nav-item dropdown">
              <a className="nav-link p-0 clear" Link to="#" data-toggle="dropdown">
                <span className="avatar w-32">
                  <img src="../images/a0.jpg" alt="..." />
                  <i className="on b-white bottom"></i>
                </span>
              </a>
              <div ui-include="/views/blocks/dropdown.user.html'"></div>
            </li>
            <li className="nav-item hidden-md-up">
              <a className="nav-link pl-2" data-toggle="collapse" data-target="#collapse">
                <i className="material-icons">&#xe5d4;</i>
              </a>
            </li>
          </ul>
        </div>
      </div>
      <div className="app-footer">
        <div className="p-2 text-xs">
          <div className="pull-right text-muted py-1">
            &copy; Copyright <strong>Flatkit</strong> <span className="hidden-xs-down">- Built with Love v1.1.3</span>
            <a ui-scroll-to="content"><i className="fa fa-long-arrow-up p-x-sm"></i></a>
          </div>
          <div className="nav">
            <Link to="/about" className="nav-link">About</Link>
            <a href="http://themeforest.net/user/flatfull/portfolio?ref=flatfull" className="nav-link" target="_blank" rel="noopener noreferrer">Get it</a>
          </div>
        </div>
      </div>
      <div ui-view className="app-body" id="view">
        <div style="min-height: 200px"></div>
      </div>
    </div>
    <div id="switcher">
      <div className="switcher box-color dark-white text-color" id="sw-theme">
        <a href ui-toggle-className="active" target="#sw-theme" className="box-color dark-white text-color sw-btn">
          <i className="fa fa-gear"></i>
        </a>
        <div className="box-header">
          <a href="https://themeforest.net/item/flatkit-app-ui-kit/13231484?ref=flatfull"
            className="btn btn-xs rounded danger pull-right">BUY</a>
          <h2>Theme Switcher</h2>
        </div>
        <div className="box-divider"></div>
        <div className="box-body">
          <p className="hidden-md-down">
            <label className="md-check m-y-xs" data-target="folded">
              <input type="checkbox" />
              <i className="green"></i>
              <span className="hidden-folded">Folded Aside</span>
            </label>
            <label className="md-check m-y-xs" data-target="boxed">
              <input type="checkbox" />
              <i className="green"></i>
              <span className="hidden-folded">Boxed Layout</span>
            </label>
            <label className="m-y-xs pointer" ui-fullscreen>
              <span className="fa fa-expand fa-fw m-r-xs"></span>
              <span>Fullscreen Mode</span>
            </label>
          </p>
          <p>Colors:</p>
          <p data-target="themeID">
            <label className="radio radio-inline m-0 ui-check ui-check-color ui-check-md"
              data-value="{primary:'primary', accent:'accent', warn:'warn'}">
              <input type="radio" name="color" value="1" />
              <i className="primary"></i>
            </label>
            <label className="radio radio-inline m-0 ui-check ui-check-color ui-check-md"
              data-value="{primary:'accent', accent:'cyan', warn:'warn'}">
              <input type="radio" name="color" value="2" />
              <i className="accent"></i>
            </label>
            <label className="radio radio-inline m-0 ui-check ui-check-color ui-check-md"
              data-value="{primary:'warn', accent:'light-blue', warn:'warning'}">
              <input type="radio" name="color" value="3" />
              <i className="warn"></i>
            </label>
            <label className="radio radio-inline m-0 ui-check ui-check-color ui-check-md"
              data-value="{primary:'success', accent:'teal', warn:'lime'}">
              <input type="radio" name="color" value="4" />
              <i className="success"></i>
            </label>
            <label className="radio radio-inline m-0 ui-check ui-check-color ui-check-md"
              data-value="{primary:'info', accent:'light-blue', warn:'success'}">
              <input type="radio" name="color" value="5" />
              <i className="info"></i>
            </label>
            <label className="radio radio-inline m-0 ui-check ui-check-color ui-check-md"
              data-value="{primary:'blue', accent:'indigo', warn:'primary'}">
              <input type="radio" name="color" value="6" />
              <i className="blue"></i>
            </label>
            <label className="radio radio-inline m-0 ui-check ui-check-color ui-check-md"
              data-value="{primary:'warning', accent:'grey-100', warn:'success'}">
              <input type="radio" name="color" value="7" />
              <i className="warning"></i>
            </label>
            <label className="radio radio-inline m-0 ui-check ui-check-color ui-check-md"
              data-value="{primary:'danger', accent:'grey-100', warn:'grey-300'}">
              <input type="radio" name="color" value="8" />
              <i className="danger"></i>
            </label>
          </p>
          <p>Themes:</p>
          <div data-target="bg" className="row no-gutter text-u-c text-center _600 clearfix">
            <label className="p-a col-sm-6 light pointer m-0">
              <input type="radio" name="theme" value="" hidden />
              Light
            </label>
            <label className="p-a col-sm-6 grey pointer m-0">
              <input type="radio" name="theme" value="grey" hidden />
              Grey
            </label>
            <label className="p-a col-sm-6 dark pointer m-0">
              <input type="radio" name="theme" value="dark" hidden />
              Dark
            </label>
            <label className="p-a col-sm-6 black pointer m-0">
              <input type="radio" name="theme" value="black" hidden />
              Black
            </label>
          </div>
        </div>
      </div>
      <div className="switcher box-color black lt" id="sw-demo">
        <a href ui-toggle-className="active" target="#sw-demo" className="box-color black lt text-color sw-btn">
          <i className="fa fa-list text-white"></i>
        </a>
        <div className="box-header">
          <h2>Demos</h2>
        </div>
        <div className="box-divider"></div>
        <div className="box-body">
          <div className="row no-gutter text-u-c text-center _600 clearfix">
            <Link to="dashboard.html" className="p-a col-sm-6 primary">
              <span className="text-white">Default</span>
            </Link>
            <Link to="dashboard.0.html" className="p-a col-sm-6 success">
              <span className="text-white">Zero</span>
            </Link>
            <Link to="dashboard.1.html" className="p-a col-sm-6 blue">
              <span className="text-white">One</span>
            </Link>
            <Link to="dashboard.2.html" className="p-a col-sm-6 warn">
              <span className="text-white">Two</span>
            </Link>
            <Link to="dashboard.3.html" className="p-a col-sm-6 danger">
              <span className="text-white">Three</span>
            </Link>
            <Link to="dashboard.4.html" className="p-a col-sm-6 green">
              <span className="text-white">Four</span>
            </Link>
            <Link to="dashboard.5.html" className="p-a col-sm-6 info">
              <span className="text-white">Five</span>
            </Link>
            <div className="p-a col-sm-6 lter">
              <span className="text">...</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
      {children} {/* Conteúdo da página específica */}
    </div>
  );
};

export default MainLayout;
