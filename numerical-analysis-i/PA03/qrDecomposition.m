% Author: Viet Duc Nguyen
% Date: 2.12.2018
%
% Program that computes the qr decomposition of a given n x m matrix.
% Input:     A ... matrix with dimension n x m
% Output:   QR ... matrix with an upper right triangle matrix,
%                  and below the diagonal, the vectors v(i) for the construction 
%                  of the householder matrices are saved v(i) = (v_i+1,...,n)
%            d ... vector that contains the missing values of the vectors v(1),...,v(n)
function [QR,d] = qrDecomposition(A)
  QR = A;
  % n ... denotes the number of rows of A
  % m ... denotes the number of columns of A
  [n,m] = size(QR);
  d = 1:m;
  for l=1:m
    % column l of matrix A
    col = QR(l:n,l);
    % compute gamma = ||col|| <--- || . || denotes the euclidian norm
    gamma = 0;
    for h=1:n-l+1
      gamma = gamma + col(h).^2;
    end
    gamma = sqrt(gamma);
    % gamma = vecnorm(col);
    
    % chose the gamma that yields the best stability
    % i.e. col(l) + gamma * e_1 != 0
    % so we chose gamma such that sign(gamma) = sign(a_1)
    if (QR(l,l) < 0)
      % if a_1 is negative, make gamma negative, too
      gamma = -gamma;
    end
    % compute the vector h that is the orthogonal vector of the hyper plane 
    % on which our column vector is reflected
    h = col + gamma * eye(size(col))(:,1);
    % compute norm of h by formular ||h|| = sqrt(2gamma*(gamma + col(l)))
    normH = sqrt(2*gamma*(gamma + col(1)));
    % normalise h
    % the resulting vector u is used to compute the householder matrices
    u = h / normH;
    % save u(l) into d(l)
    d(l) = u(1);
    % save the vectors that are used to construct the househoulder matrices
    QR(l+1:n,l) = u(2:size(u));
    % COMPUTE THE UPPER RIGHT MATRIX
    % we know that the diagonal is just -gamma since (H(j)*col(j))_j = gamma * e_j
    QR(l,l) = -gamma;
    % replace the columns j+1,...,m
    for j=l+1:m
      % QR(l:n,j) = QR(l:n,j) - 2*u*(u'*QR(l:n,j));
      g = 0;
      for k=l:n
        g = g + u(k-l+1) * QR(k,j);
      end
      g = 2*g;
      for k=l:n
        QR(k,j) =  QR(k,j) - g * u(k-l+1);
      end
    end
  end
end