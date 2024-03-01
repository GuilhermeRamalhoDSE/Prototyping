import Dashboard from '../pages/Dashboard'

function Content(){
    return (
        <div>
            <div id="content" className="app-content box-shadow-z0" role="main">
                <div className="app-header white box-shadow">
                <div className="navbar navbar-toggleable-sm flex-row align-items-center">
                    {/* Open side - Naviation on mobile */}
                    <a data-toggle="modal" data-target="#aside" className="hidden-lg-up mr-3">
                    <i className="material-icons"></i>
                    </a>
                    {/* / */}
                    {/* Page title - Bind to $state's title */}
                    <div
                    className="mb-0 h5 no-wrap"
                    ng-bind="$state.current.data.title"
                    id="pageTitle"
                    />
                    {/* navbar collapse */}
                    <div className="collapse navbar-collapse" id="collapse">
                    {/* link and dropdown */}
                    <ul className="nav navbar-nav mr-auto">
                        <li className="nav-item dropdown">
                        <a className="nav-link" href="" data-toggle="dropdown">
                            <i className="fa fa-fw fa-plus text-muted" />
                            <span>New</span>
                        </a>
                        <div ui-include="'../views/blocks/dropdown.new.html'" />
                        </li>
                    </ul>
                    <div ui-include="'../views/blocks/navbar.form.html'" />
                    {/* / */}
                    </div>
                    {/* / navbar collapse */}
                    {/* navbar right */}
                    <ul className="nav navbar-nav ml-auto flex-row">
                    <li className="nav-item dropdown pos-stc-xs">
                        <a className="nav-link mr-2" href="" data-toggle="dropdown">
                        <i className="material-icons"></i>
                        <span className="label label-sm up warn">3</span>
                        </a>
                        <div ui-include="'../views/blocks/dropdown.notification.html'" />
                    </li>
                    <li className="nav-item dropdown">
                        <a className="nav-link p-0 clear" href="#" data-toggle="dropdown">
                        <span className="avatar w-32">
                            <img src="../assets/images/a0.jpg" alt="..." />
                            <i className="on b-white bottom" />
                        </span>
                        </a>
                        <div ui-include="'../views/blocks/dropdown.user.html'" />
                    </li>
                    <li className="nav-item hidden-md-up">
                        <a
                        className="nav-link pl-2"
                        data-toggle="collapse"
                        data-target="#collapse"
                        >
                        <i className="material-icons"></i>
                        </a>
                    </li>
                    </ul>
                    {/* / navbar right */}
                </div>
                </div>
                <div className="app-footer">
                <div className="p-2 text-xs">
                    <div className="pull-right text-muted py-1">
                    © Copyright <strong>Flatkit</strong>{" "}
                    <span className="hidden-xs-down">- Built with Love v1.1.3</span>
                    <a ui-scroll-to="content">
                        <i className="fa fa-long-arrow-up p-x-sm" />
                    </a>
                    </div>
                    <div className="nav">
                    <a className="nav-link" href="../">
                        About
                    </a>
                    <a
                        className="nav-link"
                        href="http://themeforest.net/user/flatfull/portfolio?ref=flatfull"
                    >
                        Get it
                    </a>
                    </div>
                </div>
                </div>
                <div ui-view="" className="app-body" id="view">
                {/* ############ PAGE START*/}
                <Dashboard />
                {/* ############ PAGE END*/}
            </div>
            </div>
      </div>
    )
}

export default Content;
