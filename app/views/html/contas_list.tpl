% rebase('app/views/html/base.tpl', title='Contas', active_page='contas')

<section class="container">
    <div class="section-header">
        <div class="hero-badge">
            <i class="fa-solid fa-wallet"></i> Minhas Contas
        </div>
        <h2>Gerenciamento de <span class="gradient-text">Contas</span></h2>
        <p>Acompanhe seus saldos e gerencie suas contas bancárias cadastradas.</p>
    </div>

    <div class="crud-actions" style="margin-bottom: 20px; text-align: right;">
        <a href="/contas/nova" class="btn btn-primary"><i class="fa-solid fa-plus"></i> Nova Conta</a>
    </div>

    <div class="glass-card" style="padding: 20px; overflow-x: auto;">
        <table class="crud-table">
            <thead>
                <tr>
                    <th>Titular</th>
                    <th>Número da Conta</th>
                    <th>Saldo</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                % if not contas:
                <tr>
                    <td colspan="4" style="text-align: center; padding: 20px;">Nenhuma conta cadastrada.</td>
                </tr>
                % else:
                    % for c in contas:
                    <tr>
                        <td style="font-size: 0.9em; color: #888;">{{c['nome']}} {{c['sobrenome']}}</td>
                        <td><strong>{{c['numero_conta']}}</strong></td>
                        <td style="color: {{'#10b981' if c['saldo'] >= 0 else '#ef4444'}}">R$ {{"%.2f" % c['saldo']}}</td>
                        <td class="action-btns">
                            <a href="/contas/editar/{{c['id']}}" class="btn-icon" style="color: #3b82f6;" title="Editar">
                                <i class="fa-solid fa-pen"></i>
                            </a>
                            <form action="/contas/deletar/{{c['id']}}" method="POST" style="display:inline;" onsubmit="return confirm('Tem certeza que deseja deletar esta conta?');">
                                <button type="submit" class="btn-icon" style="color: #ef4444;" title="Deletar">
                                    <i class="fa-solid fa-trash"></i>
                                </button>
                            </form>
                        </td>
                    </tr>
                    % end
                % end
            </tbody>
        </table>
    </div>
</section>
