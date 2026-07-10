% rebase('app/views/html/base.tpl', title='Transações', active_page='transacoes')

<section class="container">
    <div class="section-header">
        <div class="hero-badge">
            <i class="fa-solid fa-money-bill-transfer"></i> Extrato e Histórico
        </div>
        <h2>Histórico de <span class="gradient-text">Transações</span></h2>
        <p>Acompanhe todas as movimentações financeiras das suas contas.</p>
    </div>

    <div class="crud-actions" style="margin-bottom: 20px; text-align: right;">
        <a href="/transacoes/nova" class="btn btn-primary"><i class="fa-solid fa-plus"></i> Nova Transação</a>
    </div>

    <div class="glass-card" style="padding: 20px; overflow-x: auto;">
        <table class="crud-table">
            <thead>
                <tr>
                    <th>Data/Hora</th>
                    <th>Tipo</th>
                    <th>Origem</th>
                    <th>Destino</th>
                    <th>Valor</th>
                    <th>Descrição</th>
                </tr>
            </thead>
            <tbody>
                % if not transacoes:
                <tr>
                    <td colspan="6" style="text-align: center; padding: 20px;">Nenhuma transação encontrada.</td>
                </tr>
                % else:
                    % for t in transacoes:
                    <tr>
                        <td style="font-size: 0.9em; color: #888;">{{t['data_hora']}}</td>
                        <td>
                            % if t['tipo'] == 'deposito':
                                <span class="badge badge-success"><i class="fa-solid fa-arrow-down"></i> Depósito</span>
                            % elif t['tipo'] == 'saque':
                                <span class="badge badge-danger"><i class="fa-solid fa-arrow-up"></i> Saque</span>
                            % else:
                                <span class="badge badge-info"><i class="fa-solid fa-right-left"></i> Transferência</span>
                            % end
                        </td>
                        <td>{{t['origem_str']}}</td>
                        <td>{{t['destino_str']}}</td>
                        <td style="font-weight: bold;">R$ {{"%.2f" % t['valor']}}</td>
                        <td style="font-size: 0.9em;">{{t['descricao']}}</td>
                    </tr>
                    % end
                % end
            </tbody>
        </table>
    </div>
</section>
