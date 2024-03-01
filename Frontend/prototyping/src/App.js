import Aside from './components/Aside'
import Content from './components/Content'
import Switcher from './components/Switcher'


function App(){
  return (
    <div class="app" id="app">
      <div id="aside" className="app-aside modal nav-dropdown">
          <Aside />
      </div>
      <div id="content" className="app-content box-shadow-z0" role="main">
          <Content />
          
      </div>
      <div id="switcher">
          <Switcher />
      </div>
    </div>
    
  
  );
};

export default App;
