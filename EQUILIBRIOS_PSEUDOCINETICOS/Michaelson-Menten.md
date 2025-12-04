# Modelo cinético de Michaelson-Menden

Se modela la velocidad de una reacción catalizada por enzimas. Es de uso común en biología pues se usa para describir la absorción de nutrientes por parte de células cultivadas. 

$$
E+S\overset{k_f,k_r}{\longleftrightarrow}\left[ES\right]\overset{k_c}{\longleftrightarrow} E+P
$$

La enzima $E$ interactua con el sustrato $S$ para formar un complejo $[ES]$. Posteriormente, este complejo se descompone, consumiendo el sustrato, regenerando la enzima y produciendo un producto $P$. $k_f,k_r$ son las constantes de velocidad de asociación y disociación ezima-sustrato respectivamente; $k_c$ es la constante de velocidad de disociación del complejo para la formación del producto.

## Aproximación de rápido equilibrio

La velocidad de formación de producto varía linealmente con la concentración de complejo

$$
\frac{\partial [P]}{\partial t} = k_c[ES]
$$

La condición de rápido equilibrio implica que en el estado inicial, la concentración velocidad

$$
\begin{align*}
k_f\left[E\right]\left[S\right]=k_r\left[ES\right] + k_c\left[ES\right]\longrightarrow \frac{\left[E\right]\left[S\right]}{\left[ES\right]}=\frac{k_c+k_r}{k_f}
\end{align*}
$$



## Aproximación de estado estable

La velocidad de formación de producto varía linealmente con la concentración de complejo

$$
\begin{align}
\frac{\partial [P]}{\partial t} = k_c[ES] \label{A1}
\end{align}
$$

La condición de estado estable implica que en el estado inicial, la formación y disociación de complejo suceden a la misma velocidad

$$
k_f\left[E\right]\left[S\right]=k_r\left[ES\right] + k_c\left[ES\right]\longrightarrow\left[E\right]\left[S\right]=\frac{k_c+k_r}{k_f} \left[ES\right]=k_m\left[ES\right]
$$

La concentración total de enzima en el sistema es la suma de las concentraciones de enzima libre $\left[E\right]$ y enzima fijada en los sitios activos del sustrato $\left[ES\right]$, es decir, $\left[E\right]_T=\left[E\right]+\left[ES\right]$. De donde $\left[E\right]=\left[E\right]_T-\left[ES\right]$. Así

$$
\left(\left[E\right]_T-\left[ES\right]\right)\left[S\right]=k_m\left[ES\right]\longrightarrow \left[ES\right]=\frac{\left[E\right]_T \left[S\right]}{k_m+\left[S\right]}
$$

Sustituyendo en la ecuación $\ref{A1}$
