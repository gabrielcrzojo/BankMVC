% rebase('app/views/html/base.tpl', title='Dashboard', active_page='dashboard')

<section class="container">
    <div class="section-header">
        <div class="hero-badge">
            <i class="fa-solid fa-chart-line"></i> Dashboard
        </div>
        <h2>Visão <span class="gradient-text">Geral</span></h2>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-bottom: 40px;">
        <!-- Card de Saldo -->
        <div class="glass-card" style="display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 40px;">
            <i class="fa-solid fa-wallet" style="font-size: 3rem; color: var(--primary-color); margin-bottom: 15px;"></i>
            <h3 style="color: var(--text-secondary); margin-bottom: 10px;">Saldo Total (Todas as Contas)</h3>
            <div style="font-size: 2.5rem; font-weight: bold; color: var(--text-color);">R$ {{"%.2f" % saldo_total}}</div>
        </div>

        <!-- Perfil -->
        <div class="glass-card">
            <h3><i class="fa-solid fa-user"></i> Meu Perfil</h3>
            <ul style="list-style: none; padding-top: 15px; display: flex; flex-direction: column; gap: 10px;">
                <li><strong>Nome:</strong> {{user['nome']}}</li>
                <li><strong>E-mail:</strong> {{user['email']}}</li>
                <li><strong>Tipo:</strong> {{user['tipo'].capitalize()}}</li>
            </ul>
        </div>
    </div>

    <!-- Lista de Contas -->
    <div class="glass-card" style="margin-bottom: 40px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <h3><i class="fa-solid fa-piggy-bank"></i> Minhas Contas</h3>
            <a href="/contas/nova" class="btn btn-primary"><i class="fa-solid fa-plus"></i> Nova Conta</a>
        </div>
        
        % if contas:
        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th>Número</th>
                        <th>Saldo</th>
                        <th>Ações</th>
                    </tr>
                </thead>
                <tbody>
                    % for c in contas:
                    <tr>
                        <td>{{c['numero_conta']}}</td>
                        <td style="color: var(--primary-color); font-weight: bold;">R$ {{"%.2f" % c['saldo']}}</td>
                        <td>
                            <a href="/contas/editar/{{c['id']}}" class="btn btn-secondary" style="padding: 5px 10px; font-size: 0.9rem;">Editar</a>
                        </td>
                    </tr>
                    % end
                </tbody>
            </table>
        </div>
        % else:
        <p style="text-align: center; color: var(--text-secondary); padding: 20px;">Você ainda não possui contas cadastradas.</p>
        % end
    </div>

    <!-- Últimas Transações -->
    <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <h3><i class="fa-solid fa-list-ul"></i> Últimas Movimentações</h3>
            <a href="/transacoes" class="btn btn-secondary"><i class="fa-solid fa-eye"></i> Ver Todas</a>
        </div>

        % if ultimas_transacoes:
        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th>Data/Hora</th>
                        <th>Tipo</th>
                        <th>Valor</th>
                        <th>Detalhes</th>
                    </tr>
                </thead>
                <tbody>
                    % for t in ultimas_transacoes:
                    <tr>
                        <td>{{t['data_hora']}}</td>
                        <td>
                            % if t['tipo'] == 'deposito':
                                <span style="color: #10b981;"><i class="fa-solid fa-arrow-down"></i> Depósito</span>
                            % elif t['tipo'] == 'saque':
                                <span style="color: #ef4444;"><i class="fa-solid fa-arrow-up"></i> Saque</span>
                            % else:
                                <span style="color: #3b82f6;"><i class="fa-solid fa-right-left"></i> Transferência</span>
                            % end
                        </td>
                        <td>R$ {{"%.2f" % t['valor']}}</td>
                        <td>
                            <span style="font-size: 0.9rem; color: var(--text-secondary);">
                                % if t['tipo'] == 'deposito':
                                    Para: {{t['destino_str']}}
                                % elif t['tipo'] == 'saque':
                                    De: {{t['origem_str']}}
                                % else:
                                    {{t['origem_str']}} &rarr; {{t['destino_str']}}
                                % end
                                % if t['descricao']:
                                    <br><em>{{t['descricao']}}</em>
                                % end
                            </span>
                        </td>
                    </tr>
                    % end
                </tbody>
            </table>
        </div>
        % else:
        <p style="text-align: center; color: var(--text-secondary); padding: 20px;">Nenhuma movimentação recente.</p>
        % end
    </div>
</section>
