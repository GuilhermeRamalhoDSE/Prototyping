function Switcher(){
    return (
        <div><>
        {/* theme switcher */}
        <div id="switcher">
          <div className="switcher box-color dark-white text-color" id="sw-theme">
            <a
              href=""
              ui-toggle-class="active"
              target="#sw-theme"
              className="box-color dark-white text-color sw-btn"
            >
              <i className="fa fa-gear" />
            </a>
            <div className="box-header">
              <a
                href="https://themeforest.net/item/flatkit-app-ui-kit/13231484?ref=flatfull"
                className="btn btn-xs rounded danger pull-right"
              >
                BUY
              </a>
              <h2>Theme Switcher</h2>
            </div>
            <div className="box-divider" />
            <div className="box-body">
              <p className="hidden-md-down">
                <label className="md-check m-y-xs" data-target="folded">
                  <input type="checkbox" />
                  <i className="green" />
                  <span className="hidden-folded">Folded Aside</span>
                </label>
                <label className="md-check m-y-xs" data-target="boxed">
                  <input type="checkbox" />
                  <i className="green" />
                  <span className="hidden-folded">Boxed Layout</span>
                </label>
                <label className="m-y-xs pointer" ui-fullscreen="">
                  <span className="fa fa-expand fa-fw m-r-xs" />
                  <span>Fullscreen Mode</span>
                </label>
              </p>
              <p>Colors:</p>
              <p data-target="themeID">
                <label
                  className="radio radio-inline m-0 ui-check ui-check-color ui-check-md"
                  data-value="{primary:'primary', accent:'accent', warn:'warn'}"
                >
                  <input type="radio" name="color" defaultValue={1} />
                  <i className="primary" />
                </label>
                <label
                  className="radio radio-inline m-0 ui-check ui-check-color ui-check-md"
                  data-value="{primary:'accent', accent:'cyan', warn:'warn'}"
                >
                  <input type="radio" name="color" defaultValue={2} />
                  <i className="accent" />
                </label>
                <label
                  className="radio radio-inline m-0 ui-check ui-check-color ui-check-md"
                  data-value="{primary:'warn', accent:'light-blue', warn:'warning'}"
                >
                  <input type="radio" name="color" defaultValue={3} />
                  <i className="warn" />
                </label>
                <label
                  className="radio radio-inline m-0 ui-check ui-check-color ui-check-md"
                  data-value="{primary:'success', accent:'teal', warn:'lime'}"
                >
                  <input type="radio" name="color" defaultValue={4} />
                  <i className="success" />
                </label>
                <label
                  className="radio radio-inline m-0 ui-check ui-check-color ui-check-md"
                  data-value="{primary:'info', accent:'light-blue', warn:'success'}"
                >
                  <input type="radio" name="color" defaultValue={5} />
                  <i className="info" />
                </label>
                <label
                  className="radio radio-inline m-0 ui-check ui-check-color ui-check-md"
                  data-value="{primary:'blue', accent:'indigo', warn:'primary'}"
                >
                  <input type="radio" name="color" defaultValue={6} />
                  <i className="blue" />
                </label>
                <label
                  className="radio radio-inline m-0 ui-check ui-check-color ui-check-md"
                  data-value="{primary:'warning', accent:'grey-100', warn:'success'}"
                >
                  <input type="radio" name="color" defaultValue={7} />
                  <i className="warning" />
                </label>
                <label
                  className="radio radio-inline m-0 ui-check ui-check-color ui-check-md"
                  data-value="{primary:'danger', accent:'grey-100', warn:'grey-300'}"
                >
                  <input type="radio" name="color" defaultValue={8} />
                  <i className="danger" />
                </label>
              </p>
              <p>Themes:</p>
              <div
                data-target="bg"
                className="row no-gutter text-u-c text-center _600 clearfix"
              >
                <label className="p-a col-sm-6 light pointer m-0">
                  <input type="radio" name="theme" defaultValue="" hidden="" />
                  Light
                </label>
                <label className="p-a col-sm-6 grey pointer m-0">
                  <input type="radio" name="theme" defaultValue="grey" hidden="" />
                  Grey
                </label>
                <label className="p-a col-sm-6 dark pointer m-0">
                  <input type="radio" name="theme" defaultValue="dark" hidden="" />
                  Dark
                </label>
                <label className="p-a col-sm-6 black pointer m-0">
                  <input type="radio" name="theme" defaultValue="black" hidden="" />
                  Black
                </label>
              </div>
            </div>
          </div>
          <div className="switcher box-color black lt" id="sw-demo">
            <a
              href=""
              ui-toggle-class="active"
              target="#sw-demo"
              className="box-color black lt text-color sw-btn"
            >
              <i className="fa fa-list text-white" />
            </a>
            <div className="box-header">
              <h2>Demos</h2>
            </div>
            <div className="box-divider" />
            <div className="box-body">
              <div className="row no-gutter text-u-c text-center _600 clearfix">
                <a href="dashboard.html" className="p-a col-sm-6 primary">
                  <span className="text-white">Default</span>
                </a>
                <a href="dashboard.0.html" className="p-a col-sm-6 success">
                  <span className="text-white">Zero</span>
                </a>
                <a href="dashboard.1.html" className="p-a col-sm-6 blue">
                  <span className="text-white">One</span>
                </a>
                <a href="dashboard.2.html" className="p-a col-sm-6 warn">
                  <span className="text-white">Two</span>
                </a>
                <a href="dashboard.3.html" className="p-a col-sm-6 danger">
                  <span className="text-white">Three</span>
                </a>
                <a href="dashboard.4.html" className="p-a col-sm-6 green">
                  <span className="text-white">Four</span>
                </a>
                <a href="dashboard.5.html" className="p-a col-sm-6 info">
                  <span className="text-white">Five</span>
                </a>
                <div className="p-a col-sm-6 lter">
                  <span className="text">...</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        {/* / */}
      </>
    </div>
    )
}

export default Switcher;