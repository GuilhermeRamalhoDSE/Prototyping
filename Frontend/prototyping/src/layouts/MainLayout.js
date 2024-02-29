import React from 'react';
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
      {/* Cabeçalho, barra lateral, etc. */}
      {children} {/* Conteúdo da página específica */}
      {/* Rodapé, etc. */}
    </div>
  );
};

export default MainLayout;
